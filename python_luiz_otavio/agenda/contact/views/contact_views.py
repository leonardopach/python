from contact.models import Contact
from django.shortcuts import render


def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')[0:10]

    print(contacts.query)
    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context
    )
