from django import forms
from django.forms import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import TextInput, ImageField

from .models import ProfileUser


class UserSignUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Имя пользователя"
        }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Пароль"
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "ReInputPassword",
            'placeholder': "Повторите пароль"
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']
        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class UserSignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Имя пользователя"
        }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Пароль"
        }),
    )


class ProfileUserForm(models.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('phone', 'country', 'city', 'ava', 'bio',)
        ava = ImageField()
        widgets = {
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'телефон',
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'страна',
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'city',
            }),
            'bio': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'bio',
            }),
        }
