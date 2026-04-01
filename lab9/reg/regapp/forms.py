from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password= forms.CharField(widget=forms.PasswordInput,required=False)
    emailid=forms.EmailField(required=False)
    contact= forms.CharField(max_length=10,required=False)
