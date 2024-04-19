from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('api/create/', views.UserCreateView.as_view(), name='create'),
    path('token/', views.TokenCreateView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('user-orders/<str:user_id>/', views.UserOrders.as_view(), name='user_orders'),
    path('user-orders-100/<str:user_id>/', views.UserOrders100.as_view(), name='user_orders_100'),
]