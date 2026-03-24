from django import forms

CAR_CHOICES = [
    ('Toyota','Toyota'),
    ('Honda','Honda'),
    ('BMW','BMW'),
    ('AUDI','AUDI'),
]

class CarForm(forms.Form):
    manufacturer= forms.ChoiceField(choices=CAR_CHOICES)
    model=forms.CharField(max_length=100)