# flake8: noqa
from django.shortcuts import render
from contact.forms import ContactForm


def create(request):
    if request.method == "POST":
        context = {"forms": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)
    context = {"form": ContactForm()}
    return render(
        request,
        "contact/create.html",
    )
