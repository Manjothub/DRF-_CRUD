from django.urls import path,include
from API.views import *
urlpatterns = [
    path('',HOME,name="Homepage")
]