from django.shortcuts import render, redirect
from .models import Student

def home(request):
    if request.method == "POST":
        Student.objects.create(
            student_id=request.POST.get("student_id"),
            name=request.POST.get("name"),
            course=request.POST.get("course"),
            dob=request.POST.get("dob"),
        )
        return redirect('home')

    students = Student.objects.all()
    return render(request, "home.html", {"students": students})