from django.shortcuts import render
from .forms import CgpaForm
# Create your views here.

def page1(request):
    form=CgpaForm()
    return render(request,'page1.html',{'form': form})

def page2(request):
    if request.method=="POST":
        form = CgpaForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            totalmarks=form.cleaned_data['totalmarks']
            result=totalmarks/50
            return render(request,'page2.html',{
                'name': name,
                'totalmarks': totalmarks,
                'result':result
            })
    return render(request,'page1.html',{"form": CgpaForm()})
