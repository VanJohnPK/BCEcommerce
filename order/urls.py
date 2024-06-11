from django.urls import path
from . import views
from .views import OrderListView, CategoryListView, OrderDetailView

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('', views.my_view, name='post'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('search/', views.search_order_by_phone, name='search_order_by_phone'),
    
]
