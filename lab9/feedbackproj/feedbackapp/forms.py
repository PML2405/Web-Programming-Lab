from django import forms

COURSE_CHOICES = [
    ('ASP-XML', 'ASP-XML'),
    ('DotNET', 'DotNET'),
    ('JavaPro', 'JavaPro'),
    ('Unix,C,C++', 'Unix,C,C++'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

RATING_CHOICES = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Average', 'Average'),
    ('Poor', 'Poor'),
]

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Student name")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    suggestion = forms.CharField(widget=forms.Textarea, required=False)