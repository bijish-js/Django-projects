from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def booksHome(request):
    
    return render(request,'booksHome.html')

def booksEnter(request):
    
    return render(request,'booksEnter.html')

def enterOpr(request):
    accno=request.POST['accno']
    title=request.POST['title']
    author=request.POST['author']

    #record creation in db
    obj=Book()
    obj.accno=accno
    obj.title=title
    obj.author=author
    obj.save()
    
    return render(request,'RecordAdded.html')

def booksSearch(request):
    
    return render(request,'booksSearch.html')

def searchOpr(request):
    searchText=request.POST['searchtext']
    result = Book.Objects.filter(title__contains=searchText)
    print(result)
    return render(request,'booksSearchDisplay.html',{'books':result})
