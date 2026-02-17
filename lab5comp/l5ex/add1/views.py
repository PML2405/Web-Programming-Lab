from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def q1(request):
    return render(request,'q1.html')

def q2(request):
    return render(request,'q2.html')

def h1(request):
    return render(request,'h1.html')
