from django.urls import path
from . import views

app_name = 'customer'

urlpatters = [
    path('', views.menu_list, name='menu_list'),'
]