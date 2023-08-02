from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a",
                "placeholder": "Aqui veio do init",
            }
        ),
        label="primeiro nome",
        help_text="Texto de ajuda para seu usuário",
    )

    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
        )
<<<<<<< HEAD
        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={"class": "class a", "placeholder": "Escreva seu primeiro nome"}
        #     )
        # }
=======
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Escreva seu primeiro nome"}
            )
        }
>>>>>>> 41a59d823e4c64362409c4cee91ec396eab83fc6

    def clean(self):
        # cleaned_data = self.cleaned_data
        self.add_error(None, ValidationError("Mensagem de erro", code="invalid"))
        self.add_error(None, ValidationError("Mensagem de erro", code="invalid"))
        self.add_error(None, ValidationError("Mensagem de erro", code="invalid"))
        return super().clean()
