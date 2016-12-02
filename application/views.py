# coding:utf-8
from annoying.decorators import ajax_request, render_to
import pandas as pd
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import ResponsiblePersons, FixedAssets
import json
from django.shortcuts import redirect


def custom_login(request):
    if not request.user.is_authenticated():
        return redirect('/responsible_persons')


@csrf_exempt
@render_to('responsible_persons.html')
def responsible_persons(request):
    return {'section': 'responsible_persons'}


@ajax_request
def person_search(request):

    query = request.GET.get('search_query', '')
    search_data = ResponsiblePersons.objects.filter(Q(full_name__icontains=query) | Q(
        residence_street__icontains=query) | Q(phone_number__icontains=query))\
        .values('full_name', 'residence_street', 'salary', 'premium', 'phone_number')

    df = pd.DataFrame.from_records(search_data, coerce_float=True)
    if not df.empty:
        df = df.head(1000)
        df = df.sort_values('full_name')
        df = df[['full_name', 'residence_street', 'phone_number', 'salary', 'premium']]
        df = df.rename(columns={'full_name': u"Прізвище, Ім'я, По-батькові",
                                'phone_number': u'Номер телефону', 'salary': u'Зарплата',
                                'premium': u'Премія', 'residence_street': u'Адреса'})
        df = df.to_dict('split')
        del df['index']
        return df
    else:
        empty_df = pd.DataFrame().to_dict('split')
        del empty_df['index']
        return empty_df


@csrf_exempt
@render_to('fixed_assets.html')
def fixed_assets(request):
    all_data = FixedAssets.objects.values('name', 'price', 'inventory_number', 'start_date', 'end_date',
                                          'placement__country', 'placement__city', 'placement__street',
                                          'placement__home_number', 'departament__departament_name',
                                          'persons__full_name')
    rename_dict = {'name': u"Назва основного засобу", 'price': u"Ціна", 'inventory_number': u"Інвентарний номер",
                   'start_date': u"Дата введення в експлуатацію",
                   'end_date': u"Прогнозована дата виведення з експлуатації", 'placement': u"Розміщення",
                   'departament__departament_name': u"Назва департаменту, до якого належить",
                   'persons__full_name': u"Ім'я відповідальної особи"}

    df = pd.DataFrame.from_records(all_data, coerce_float=True)
    df['placement'] = df['placement__country'] + ' / ' + df['placement__city'] + ' / ' + df['placement__street']
    df['start_date'] = df['start_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df['end_date'] = df['end_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df = df[['name', 'price', 'inventory_number', 'start_date', 'end_date', 'placement',
             'departament__departament_name', 'persons__full_name']]
    df = df.rename(columns=rename_dict)
    data = df.to_dict('split')
    return {'section': 'fixed_assets', 'data': json.dumps(data, ensure_ascii=True).encode('utf-8')}
