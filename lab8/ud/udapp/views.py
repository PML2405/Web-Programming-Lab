from django.shortcuts import render, redirect
from .forms import StudentForm

def firstPage(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']

            return redirect('second')

    return render(request, 'firstPage.html', {'form': form})


def secondPage(request):
    name = request.session.get('name')
    roll = request.session.get('roll')
    subject = request.session.get('subject')

    return render(request, 'secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })