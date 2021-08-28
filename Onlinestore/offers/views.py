from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product

# Create your views here.
def home(request):
    # products=Product.Objects.all()
    # return render(request,'index.html',{'products':products})
    # return HttpResponse("<h1>Welcome</h1>")
    return render(request,'home.html',{'name':'Bijish'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'res':res})
