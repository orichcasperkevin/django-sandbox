from django.contrib import admin

from students.models import Student, Year

# Register your models here.
admin.site.register(Year)
admin.site.register(Student)