from django.shortcuts import render
from .forms import ShopForm

def home(request):
    form = ShopForm()
    total = None
    brand = None
    items = None
    qty = None

    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            items = form.cleaned_data['item']
            qty = form.cleaned_data['qty']

            price = 0
            if 'Mobile' in items:
                price += 10000
            if 'Laptop' in items:
                price += 50000

            total = price * qty

            return render(request, 'bill.html', {
                'brand': brand,
                'items': items,
                'qty': qty,
                'total': total
            })

    return render(request, 'home.html', {'form': form})