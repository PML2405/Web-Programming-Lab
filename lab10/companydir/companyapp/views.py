from django.shortcuts import render
from .models import Works, Lives
from .forms import WorksForm, SearchForm

# Insert into WORKS
def add_work(request):
    form = WorksForm()
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'add_work.html', {'form': form})


# Search people by company
def search_company(request):
    results = []
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']

            works = Works.objects.filter(company_name=company)

            for w in works:
                try:
                    l = Lives.objects.get(person_name=w.person_name)
                    results.append((w.person_name, l.city))
                except:
                    results.append((w.person_name, "No city"))

    return render(request, 'search.html', {'form': form, 'results': results})