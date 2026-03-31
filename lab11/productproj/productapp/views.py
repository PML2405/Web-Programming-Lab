from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def index(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    products = Product.objects.all()

    return render(request, 'index.html', {
        'form': form,
        'products': products
    })