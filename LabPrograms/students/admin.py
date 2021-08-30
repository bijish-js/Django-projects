from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('idno','name','mark1','mark2','mark3')

# Register your models here.

admin.site.register(Student,StudentAdmin)

