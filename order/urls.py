from django.urls import path
from . import views
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('orders/', OrderListView.as_view(), name='order_list'),
 
    path('', views.my_view, name='post'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    
    path('search/', views.search_order, name='search_order'),
    path('orders/<int:order_id>/mark_accepted/', views.mark_order_as_accepted, name='mark_order_as_accepted'),
    path('orders/pending/', views.list_orders_pending_approval, name='list_orders_pending_approval'),
]
