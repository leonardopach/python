from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request,
        "home/index.html",
        {"texto": "Estamos na home", "title": "titulo do home"},
    )
