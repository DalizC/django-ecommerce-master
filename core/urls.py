from django.urls import path, re_path
from .views import item_list
from core import views


app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    re_path(r'^item$', views.itemApi)
]
