from django import forms

class CgpaForm(forms.Form):
    name=forms.CharField(max_length=50)
    totalmarks=forms.IntegerField()