from django.urls import path
from . import views
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('orders/', OrderListView.as_view(), name='order_list'),
 
    #order view
    path('', views.my_view, name='post'),
    #path('card_view', views.card_view, name='card_view'),
    path('detail_view/<int:id>/', views.detail_view, name='detail_view'),

####order
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    
    path('search/', views.search_order, name='search_order'),
    path('orders/<int:order_id>/mark_accepted/', views.mark_order_as_accepted, name='mark_order_as_accepted'),
    path('orders/pending/', views.list_orders_pending_approval, name='list_orders_pending_approval'),
    path('orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('post/<int:order_id>/', views.post, name='post_with_id'),

#search
    path('orders/search_order_list/', views.search_order_list, name='search_order_list'),

]
