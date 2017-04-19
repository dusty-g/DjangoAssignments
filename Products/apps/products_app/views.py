from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):

    Product.objects.create(name = 'Hammer', description = 'a tool for hammering', weight = 18.3, price = 12.33, cost = 8.76, category = 'tools')
    Product.objects.create(name = 'Screwdriver', description = 'a tool for hammering', weight = 18.3, price = 12.33, cost = 8.76, category = 'tools')
    Product.objects.create(name = 'Wrench', description = 'a tool for hammering', weight = 18.3, price = 12.33, cost = 8.76, category = 'tools')
    products = Product.objects.all()
    for i in products:
        print i.name
    return render(request, 'products_app/index.html')