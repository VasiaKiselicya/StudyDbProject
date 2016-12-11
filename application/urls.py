from django.conf.urls import url
from .views import responsible_persons, person_search, fixed_assets, custom_login, personal_card

urlpatterns = [
    url(r'^responsible_persons/$', responsible_persons, name='responsible_persons'),
    url(r'^person_search/$', person_search, name='person_search'),
    url(r'^fixed_assets/$', fixed_assets, name='fixed_assets'),
    url(r'^$', custom_login),
    url(r'^personal_card/', personal_card, name='personal_card')
]
