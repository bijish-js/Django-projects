from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def studentsHome(request):
    
    return render(request,'studentsHome.html')

def studentsEnter(request):
    
    return render(request,'studentsEnter.html')

def enterOpr(request):
    
    idno=request.POST['idno']
    name=request.POST['name']
    mark1=int(request.POST['mark1'])
    mark2=int(request.POST['mark2'])
    mark3=int(request.POST['mark3'])

    #record creation in db
    obj=Student()
    obj.idno=idno
    obj.name=name
    obj.mark1=mark1
    obj.mark2=mark2
    obj.mark3=mark3

    obj.save()
    
    return render(request,'RecordAdded.html')

def studentsGrade(request):
   
    return render(request,'studentsGrade.html')

def gradeOpr(request):
    idno=request.POST['idno']
    res = Student.Objects.get(idno=idno)
    avg=(res.mark1+res.mark2+res.mark3)/3
    if(avg>80):
        grade='A'
    elif(avg>60):
        grade='B'
    elif(avg>40):
        grade='C'
    else:
        grade='D'
    res.avg=round(avg, 2)
    res.grade=grade
    print(res.name)
    return render(request,'studentGradeDisplay.html',{'student':res})

