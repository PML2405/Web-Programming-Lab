from django import forms

BRAND_CHOICES = [
    ('HP', 'HP'),
    ('Nokia', 'Nokia'),
    ('Samsung', 'Samsung'),
    ('Motorola', 'Motorola'),
    ('Apple', 'Apple'),
]

ITEM_CHOICES = [
    ('Mobile', 'Mobile'),
    ('Laptop', 'Laptop'),
]

class ShopForm(forms.Form):
    brand = forms.ChoiceField(choices=BRAND_CHOICES, widget=forms.RadioSelect)
    item = forms.MultipleChoiceField(choices=ITEM_CHOICES, widget=forms.CheckboxSelectMultiple)
    qty = forms.IntegerField(min_value=1)