from django.urls import path
from config_generator.configurator.views import sign_in_view, site_view, create_config,\
    create_app, get_resources, logout_view, get_config, sign_up_view
from django.conf.urls import url


urlpatterns = [
    url(r"^signin/$", sign_in_view, name="signin"),
    url(r"^signup/$", sign_up_view, name="signup"),
    url(r"^logout/$", logout_view, name="logout"),
    url(r"^$", site_view, name="site"),
    url(r"^create_app/$", create_app, name="create_app"),
    url(r"^create_config/$", create_config, name="create_config"),
    path('api/configuration/', get_config, name='get_config'),
    path('api/resources/', get_resources, name='get_resources'),
]
