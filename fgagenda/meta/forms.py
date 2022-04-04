from django import forms
from .models import Meta
from django.utils import timezone

class MetaForm(forms.ModelForm):

    class Meta:
        model = Meta
        fields = [
            'nome',
            'descricao',
            'dataFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-meta-input",
                'placeholder': 'Nome da Meta'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-meta-input",
                'placeholder': 'Descrição'
            }),
            'dataFim': forms.DateTimeInput(attrs={  # Consertar "type" de dataFim, pois é possível criar
                'type': "datetime-local",           # uma Meta com data de um dia anterior!
                'class': "criar-meta-input",
                'placeholder': timezone.now()
            }),
        }
    