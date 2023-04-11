from django.forms import models
from django.forms import TextInput

from .models import TextToCreateImg


class KeysWordsForm(models.ModelForm):
    class Meta:
        model = TextToCreateImg
        fields = ('gender', 'skin_color', 'age', 'hair', 'eyes', 'eyebrows', 'jaw', 'nose')
        widgets = {
            'gender': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'пол',
            }),
            'skin_color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'цвет кожи',
            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'возраст',
            }),
            'hair': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'причестка',
            }),
            'eyes': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'глаза',
            }),
            'eyebrows': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'брови',
            }),
            'jaw': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'челюсть',
            }),
            'nose': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'нос',
            }),
        }
