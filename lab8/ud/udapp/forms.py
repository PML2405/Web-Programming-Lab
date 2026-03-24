from django import forms

SUBJECT_CHOICES = [
    ('Math', 'Math'),
    ('Physics', 'Physics'),
    ('CS', 'CS'),
]

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    roll = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)