from django.urls import path, re_path
from core import views
from .views import (
    HomeView,
    StoreView
)


app_name = 'core'

urlpatterns = [
    #path('', item_list, name='item-list'),
    path('', HomeView.as_view(), name='home'),
    path('store/', StoreView.as_view(), name='store'),
    re_path(r'^item$', views.itemApi)
]
