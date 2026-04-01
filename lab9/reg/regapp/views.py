from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def register(request):
    form=UserForm()
    return render(request,'register.html',{'form':form})

def success(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            # password=form.cleaned_data['password']
            emailid=form.cleaned_data['emailid']
            contact=form.cleaned_data['contact']

            return render(request,'success.html',{
                'username': username,
                'emailid': emailid,
                'contact': contact
            })
        
    return render(request,'register.html',{'form': UserForm()})