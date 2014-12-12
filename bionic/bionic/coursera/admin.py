from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    class Meta:
        model = Student

admin.site.register(Student, StudentAdmin)