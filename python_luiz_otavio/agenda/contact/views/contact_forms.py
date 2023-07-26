# flake8: noqa
from typing import Any, Dict

from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
# from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

    def clean(self) -> Dict[str, Any]:
        cleaned_data = self.cleaned_data
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()


def create(request):
    if request.method == 'POST':
        context = {
            'forms': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html',
    )
