from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    form = FeedbackForm()
    message = ""

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = f"Thanks {name} for your feedback."

    return render(request, 'feedback.html', {
        'form': form,
        'message': message
    })