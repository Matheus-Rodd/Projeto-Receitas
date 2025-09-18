from django import forms
from .models import Mensagem


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["nome", "email", "mensagem"]
        widgets = {
            "mensagem": forms.Textarea(attrs={"rows": 5}),
        }
