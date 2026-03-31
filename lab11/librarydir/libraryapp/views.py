from django.shortcuts import render
from .models import Author, Publisher, Book
from .forms import AuthorForm, PublisherForm, BookForm

def home(request):
    aform = AuthorForm()
    pform = PublisherForm()
    bform = BookForm()

    if request.method == 'POST':
        if 'author' in request.POST:
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()

        elif 'publisher' in request.POST:
            form = PublisherForm(request.POST)
            if form.is_valid():
                form.save()

        elif 'book' in request.POST:
            form = BookForm(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                book.save()
                form.save_m2m()

    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    books = Book.objects.all()

    return render(request, 'home.html', {
        'aform': aform,
        'pform': pform,
        'bform': bform,
        'authors': authors,
        'publishers': publishers,
        'books': books
    })