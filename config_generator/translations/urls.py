from django.urls import path
from config_generator.translations.views import get_translations, change_keys
from django.conf.urls import url


urlpatterns = [
    path('api/translations/<lang>/', get_translations, name='get_translations'),
    path('keys_list/', change_keys, name='change_keys_list'),
]
