from django.shortcuts import render
from .models import Institutes

def show_institutes(request):
    institutes = Institutes.objects.all()

    return render(request, 'index.html', {
        'institutes': institutes
    })