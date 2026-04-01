from django.shortcuts import render, redirect 

from .models import Student 

from .forms import StudentForm 

 

def add_student(request): 

    form = StudentForm() 

    if request.method == 'POST': 

        form = StudentForm(request.POST) 

        if form.is_valid(): 

            form.save() 

            return redirect('show_students') 

 

    return render(request, 'add_student.html', {'form': form}) 

 

def show_students(request): 

    students = Student.objects.all() 

    return render(request, 'show_students.html', {'students': students}) 

 