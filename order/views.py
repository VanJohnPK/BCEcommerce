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


# http://localhost:8000/search/?phone_number=12345678910
def search_order_by_phone(request):
    phone_number = request.GET.get('phone_number')
    if phone_number:
        orders = Order.objects.filter(poster_phone_number=phone_number)
    else:
        orders = Order.objects.none()  # 如果没有提供电话号码，返回空查询集
    
    return render(request, 'order_list.html', {'orders': orders})


def post(request):
    form ={"name":"elman"}
    return render(request, 'post.html', {'form': form})
