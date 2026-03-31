from django.shortcuts import render, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm

# Add Category
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    return render(request, 'add_category.html', {'form': form})


# Add Page
def add_page(request):
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    return render(request, 'add_page.html', {'form': form})


# Display Data
def show_data(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'show_data.html', {
        'categories': categories,
        'pages': pages
    })