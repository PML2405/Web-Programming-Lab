from django.shortcuts import render

ITEMS = {
    'Wheat': 40,
    'Jaggery': 60,
    'Dal': 80
}

def grocery(request):
    selected_items = {}

    if request.method == 'POST':
        selected = request.POST.getlist('items')

        for item in selected:
            selected_items[item] = ITEMS[item]

    return render(request, 'grocery.html', {
        'items': ITEMS,
        'selected_items': selected_items
    })