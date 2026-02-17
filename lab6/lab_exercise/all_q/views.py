from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic.html')

def q1(request):
    return render(request,'q1.html')

def q2(request):
    return render(request,'q2.html')

def q3(request):
    return render(request,'q3.html')

def q3_metadata(request):
    return render(request,'q3_metadata.html')

def q3_publisher(request):
    return render(request,'q3_publisher.html')

def q3_reviews(request):
    return render(request,'q3_reviews.html')