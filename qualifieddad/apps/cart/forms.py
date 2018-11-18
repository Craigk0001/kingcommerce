from django import forms
from django.forms import ModelForm
from apps.cart.models import CartSelection
from apps.product_catalogue.models import Product
from . import models

class AddItemForm(forms.ModelForm):
    class Meta:
        model = CartSelection

        widgets = {'quantity':forms.NumberInput(
            attrs={

                'class':'form-control',
            }
        ),
        }

        fields = ('cart', 'product', 'quantity',)
