from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', menu, name='menu'),
]