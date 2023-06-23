from django.urls import path, re_path
from core import views
from .views import (
    HomeView,
    StoreView,
    ItemDetailView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart
)


app_name = 'core'

urlpatterns = [
    #path('', item_list, name='item-list'),
    path('', HomeView.as_view(), name='home'),
    path('store/', StoreView.as_view(), name='store'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    re_path(r'^item$', views.itemApi)
]
