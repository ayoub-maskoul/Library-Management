from django import forms
from .models import *

class CatForm (forms.ModelForm):
    class Meta:
        model = Category
        fields= ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'auther',
            'photo_book',
            'photo_auther',
            'pages',
            'price',
            'retal_price_day',
            'real_period',
            'total_rented',
            'status',
            'category',
            ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'auther':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_auther':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rentedday'}),
            'real_period':forms.NumberInput(attrs={'class':'form-control','id':'rentedprice'}),
            'total_rented':forms.NumberInput(attrs={'class':'form-control','id':'totalprice'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
