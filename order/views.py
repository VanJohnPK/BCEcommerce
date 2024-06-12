from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Order
from django.shortcuts import redirect

def hello_world(request):
    return HttpResponse("Hello, world!")

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'  # 指定模板文件的路径，默认使用 app_name/model_name_list.html
    context_object_name = 'orders'  # 设置上下文变量名称，默认为 object_list

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

from django.db.models import Q
# http://localhost:8000/search/?query=12345678910
def search_order(request):
    query = request.GET.get('query')
    orders = []

    if query:
        # 在标题、描述和类别名称中进行查询
        orders = Order.objects.filter(
            Q(title__icontains=query) |
            Q(price__iexact=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(poster_phone_number__icontains=query) 
        ).distinct()

    return render(request, 'order_list.html', {'orders': orders})

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def mark_order_as_accepted(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_accepted = True
    order.save()
    return JsonResponse({'status': 'success', 'message': f'Order {order_id} has been marked as accepted.'})

def list_orders_pending_approval(request):
    pending_orders = Order.objects.filter(is_accepted=False)
    return render(request, 'order_list.html', {'orders': pending_orders})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return JsonResponse({'status': 'success', 'message': f'Order {order_id} has been deleted.'})

def post(request, order_id=None):
    if order_id:
        order = get_object_or_404(Order, id=order_id)
    else:
        order = None

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Order saved successfully.'})
    else:
        form = OrderForm(instance=order)

    return render(request, 'post.html', {'form': form})



def post(request):
   
    form ={"name":"elman"}
    return render(request, 'post.html', {'form': form})



# views.py
from django.shortcuts import render
from .forms import OrderForm

def my_view(request):
    if request.method == 'POST':
        print("hello world")
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect or render success page
            print("data saved")
    else:
        form = OrderForm()
    return render(request, 'post.html', {'form': form})


def card_view(request):
    orders = [
        {"title": "Item 1", "description": "Description for item 1", "price": "2323", "category":"3434"},
        {"title": "Item 2", "description": "Description for item 2",  "price": "2323", "category":"3434"},
        {"title": "Item 3", "description": "Description for item 3",  "price": "2323", "category":"3434"},
        {"title": "Item 4", "description": "Description for item 4",  "price": "2323", "category":"3434"},
        {"title": "Item 5", "description": "Description for item 5",  "price": "2323", "category":"3434"},
        {"title": "Item 6", "description": "Description for item 6",  "price": "2323", "category":"3434"},
        # Add more items as needed
    ]
    return render(request, 'cards.html', {'orders': orders})


def detail_view(request,id):
    order = {"title": "Item 1", "description": "Description for item 1", "price": "2323", "poster_phone_number": "34343", "category":"fdasf"}
    return render(request, 'postdetail.html', {'order': order} )



from django.db.models import Q
# http://localhost:8000/search/?query=12345678910
def search_order_list(request):
    query = request.GET.get('query')
    orders = []

    if query:
        # 在标题、描述和类别名称中进行查询
        orders = Order.objects.filter(
            Q(title__icontains=query) |
            Q(price__iexact=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(poster_phone_number__icontains=query) 
        ).distinct()

    return render(request, 'search_order_list.html', {'orders': orders})
