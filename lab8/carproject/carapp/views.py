from django.shortcuts import render
from .forms import CarForm
# Create your views here.
def home(request):
    form=CarForm()
    return render(request,'home.html',{'form': form})
def result(request):
    if request.method == "POST":
        form=CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']

            return render(request,'result.html',{
                'manufacturer': manufacturer,
                'model': model
            })
    return render(request,'home.html',{'form': CarForm()})