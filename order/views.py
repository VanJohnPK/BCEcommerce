from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Order, Category 

def hello_world(request):
    return HttpResponse("Hello, world!")

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'  # 指定模板文件的路径，默认使用 app_name/model_name_list.html
    context_object_name = 'orders'  # 设置上下文变量名称，默认为 object_list

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'