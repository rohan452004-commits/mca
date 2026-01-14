from django.shortcuts import render, redirect
from .models import Student, Course

def landing(request):
    return render(request, 'studentmgmt/landing.html')


def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count()
    }
    return render(request, 'studentmgmt/dashboard.html', context)


def students(request):
    data = {
        'students': Student.objects.all(),
        'courses': Course.objects.all()
    }
    return render(request, 'studentmgmt/students.html', data)

def add_student(request):
    if request.method == 'POST':
        course_id = request.POST.get('course')

        if course_id:  # safety check
            Student.objects.create(
                full_name=request.POST.get('name'),
                email=request.POST.get('email'),
                age=request.POST.get('age'),
                course_id=course_id
            )

    return redirect('students')



def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('students')


def courses(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'])
    return render(request, 'studentmgmt/courses.html', {
        'courses': Course.objects.all()
    })


def delete_course(request, id):
    Course.objects.get(id=id).delete()
    return redirect('courses')
