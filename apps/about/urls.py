from django.urls import path
from .views import *



urlpatterns = [
    path('get_team/',get_team, name= "teams"),
    path('team/', TeamApi.as_view(), name='text'),
    path('alumini/', Alumini.as_view(), name='text'),
]
