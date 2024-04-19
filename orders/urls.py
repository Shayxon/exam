from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history/', views.history, name='history'),
    path('api/orderitem/', views.OrderItemView.as_view(), name='order_item'),
    path('api/order/', views.OrderView.as_view(), name='order'),
    path('api/total/', views.OrderItemTotal.as_view(), name='order_item_total'),
]