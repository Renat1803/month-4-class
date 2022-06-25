from django.shortcuts import render
from main.models import Product, Category, Tag
# Create your views here.

def index(request):
    dict_ = {
        'key': 'Hello World',
        'color': '#d534eb',
        'list_': ['Merci', "French", 'lala']
    }
    return render(request, 'index.html', context=dict_)

def product_list_view(request):
    # products = Product.objects.all() #QuerySet
    context = {
        'product_list': Product.objects.all(),
        'category_list': Category.objects.all()
    }
    # print(products)
    return render(request, 'products.html', context=context)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render (request, 'detail.html', context={'product_detail': product})

def category_product_filter_view(request, category_id):
    context = {
        'product_list': Product.objects.filter(category_id=category_id),
        'category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)