from django.contrib import admin
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'age', 'course')
    search_fields = ('full_name', 'email')
    list_filter = ('course',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
