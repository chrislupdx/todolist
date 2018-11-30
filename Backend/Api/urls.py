from django.conf.urls import url, include
from rest_framework.authtoken import views as drf_views
from django.urls import include, path


urlpatterns = [
    path('', include('Backend.urls')),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
]
