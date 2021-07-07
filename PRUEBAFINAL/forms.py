from django import forms
from django.forms import fields, widgets
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
                
        widgets ={
        'Nombre':forms.TextInput(attrs={
            'autofocus': 'autofocus',
            'class':'form-control',
        }),
        'descripcion':forms.Textarea(attrs={
            'cols':80,
            'rows':5,
            'id':"textarea",
        }),
        'categoria':forms.Select(attrs={
            'class':'form-control',
            'id':'cat',
        })
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'form-control','autofocus': 'autofocus',}), max_length=254, required=True)
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length=30, required=True)

    class Meta:
        model= User
        fields=['email','username','password1','password2']

    """  widgets ={
        'username':forms.TextInput(attrs={
            'autofocus': 'autofocus',
            'class':'form-control',
            'placeholder':'Nombre',
        })
        } """

