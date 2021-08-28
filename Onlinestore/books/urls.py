from django.urls import path
from .import views

urlpatterns = [
    path('', views.booksHome,name='booksHome'),
    path('enter', views.booksEnter,name='booksEnter'),
    path('enterOpr', views.enterOpr,name='enterOpr'),

    path('search', views.booksSearch,name='booksSearch'),
    path('searchOpr', views.searchOpr,name='searchOpr')

]