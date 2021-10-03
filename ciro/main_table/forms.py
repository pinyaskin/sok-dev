from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.models import User
from .models import Posts


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateNumberForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['callerid', 'address', 'post_number', 'name_object', 'category']

        widgets = {
            "callerid": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'SIP-Номер'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес объекта'
            }),
            "post_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер поста'
            }),
            "name_object": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название объекта'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория (нужна для фильтра)'
            }),
        }