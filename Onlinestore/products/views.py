from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products=Product.Objects.all()
    return render(request,'index.html',{'products':products})
    # return HttpResponse("<h1>Wecome to products</h1>")
