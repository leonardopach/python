# flake8: noqa
from contact.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
# from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


def create(request):
    
    context = {
        'site_title': 'Contatos'
    }
    return render(
        request,
        'contact/create.html',
        context
    )