from django.urls import path, re_path
from core import views
from .views import (
    HomeView,
    StoreView,
    ItemDetailView,
    OrderSummaryView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CheckoutView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    webpay_transaction,
    validate_transaction
)


app_name = 'core'

urlpatterns = [
    #path('', item_list, name='item-list'),
    path('', HomeView.as_view(), name='home'),
    path('store/', StoreView.as_view(), name='store'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    #path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('webpay/', webpay_transaction, name='webpay'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    # webpay_response
    path('webpay_response/', validate_transaction, name='webpay_reponse'),
    re_path(r'^item$', views.itemApi)
]
