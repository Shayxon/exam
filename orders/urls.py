from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orderitem', views.ManageOrderItemView)
router.register('order', views.ManageOrderView)

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history/', views.history, name='history'),
    path('api/total/', views.OrderItemTotal.as_view(), name='order_item_total'),
    path('api/', include(router.urls)),
]