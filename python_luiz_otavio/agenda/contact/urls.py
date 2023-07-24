# type: ignore
from contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),

    # Contact
    path("contact/<int:contact_id>/detail", views.contact, name="contact"),
    path("contact/create/", views.create, name="create"),
]
