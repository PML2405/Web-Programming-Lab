from django.shortcuts import render, redirect
from .models import Human

def home(request):
    humans = Human.objects.all()
    selected_human = None

    if request.method == "POST":
        id = request.POST.get("id")

        if id:
            selected_human = Human.objects.get(id=id)

        # UPDATE
        if "update" in request.POST:
            selected_human.last_name = request.POST.get("last_name")
            selected_human.phone = request.POST.get("phone")
            selected_human.address = request.POST.get("address")
            selected_human.city = request.POST.get("city")
            selected_human.save()
            return redirect('home')

        # DELETE
        if "delete" in request.POST:
            selected_human.delete()
            return redirect('home')

    return render(request, "home.html", {
        "humans": humans,
        "selected": selected_human
    })