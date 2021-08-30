from django.shortcuts import render

# Create your views here.

def projectHome(request):
    
    return render(request,'projectHome.html')