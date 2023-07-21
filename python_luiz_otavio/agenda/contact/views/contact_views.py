# flake8: noqa
from contact.models import Contact
from django.db.models import Q
# from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')[0:10]

    # print(contacts.query)
    context = {
        'contacts': contacts,
        'site_title': 'Contatos'
    }
    return render(
        request,
        'contact/index.html',
        context
    )


def search(request):
    # strip remove espaço do começo e fim
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect("contact:index")
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value)
        )\
        .order_by('-id')

    # print(contacts.query)
    context = {
        'contacts': contacts,
        'site_title': 'Contatos'
    }
    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # if single_contact is None:
    #     raise Http404
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }
    return render(
        request,
        'contact/contact.html',
        context
    )
