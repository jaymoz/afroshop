from django.urls import path
from . import views
from .views import *

from django.contrib import admin

urlpatterns = [
	path('',views.home, name='home'),
	path('store/',views.store, name='store'),
	path('add-to-cart/<slug>/',views.add_to_cart, name='add'),
	path('remove-from-cart/<slug>/',views.remove_from_cart, name='remove'),
	path('remove-item-from-cart/<slug>/',views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
	path('cart/',views.cart,name='cart'),
	path('add-to-cart-page/<slug>/',views.add_to_cart_page, name='add-to-cart-page'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
	path('remove-from-cart-page/<slug>/',views.remove_from_cart_page, name='remove-from-cart-page'),
	path('remove-item-from-cart-page/<slug>/',views.remove_single_item_from_cart_page, name='remove-single-item-from-cart-page'),
	path('dashboard/<str:pk>/',  views.dashboard, name = 'dashboard'),
	path('dashboard-profile/<str:pk>/', views.dash_profile, name = 'dash-profile'),
	path('dashboard-orders/<str:pk>/',views.dash_order, name = 'dash-order'),
	path('order-detail/<str:pk>/', views.order_detail, name='order-detail'),
	path('refunds/<str:pk>/', views.refund_order, name = 'ref'),
	path('cancel-order/<str:pk>/', views.cancel_order, name = 'cancel-order'),
	path('address/<str:pk>/', views.address, name="address-list"),
	path('add-address/<str:pk>/', views.add_address, name="add-address"),
	path('edit-address/<str:pk>/', views.edit_address, name="edit-address"),
	path('set-default-address/<str:pk>/', views.set_default_address, name="set-default-address"),
	path('delete-address/<str:pk>/', views.delete_address, name="delete-address"),
    path('store-category<str:pk>/', views.store_detail, name='category'),
	path('item-detail/<str:pk>/', views.item_detail, name='item-detail'),
	path('item-detail-add-to-cart/<slug>/',views.add_to_cart_item_detail_page, name='add-item'),
	path('item-detail-remove-from-cart/<slug>/',views.remove_from_cart_item_detail_page, name='remove-item'),
    path("delete-review/<str:id>/", views.delete_review, name="delete-review"),
    path("payment/", views.payment, name="payment"),
    path("payment-success/", views.payment_success, name="payment-success"),
    path("payment-failed/", views.payment_failed, name="payment-fail"),
    path("payment-checkout-complete/", views.payment_checkout_complete, name="payment-checkout")
]