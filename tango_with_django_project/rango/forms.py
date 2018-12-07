# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from .models import Category, Page, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           widget=forms.TextInput(
                                attrs={
                            'class':'form-control',
            'placeholder':'Categoria',
            'autofocus':'true'
        }
    ))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm( forms.ModelForm ):
    title = forms.CharField(max_length=128,
                            help_text="Título da página: ")
    url = forms.URLField(max_length=200,
                         help_text="URL da página: ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data

        url = cleaned_data.get('url')
        if url and not url.startswith('https://'):
            url = 'https://' + url
            cleaned_data['url'] = url
            return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Senha',
            'required':'true'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Usuário',
            'required':'true',
            'autofocus':'true'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Email',
            'required':'true'
        }
    ))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    website = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Website',
            'required':'true'
        }
    ))
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')