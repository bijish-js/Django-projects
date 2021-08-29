from django.urls import path
from .import views

urlpatterns = [
    path('', views.studentsHome,name='studentsHome'),
    path('studententer', views.studentsEnter,name='studentEnter'),
    path('enterOpr', views.enterOpr,name='enterOpr'),
    path('studentgrade', views.studentsGrade,name='studentgrade'),
    path('gradeOpr', views.gradeOpr,name='gradeOpr'),



   
]