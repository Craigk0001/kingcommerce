from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ChangeNameForm(UserChangeForm):

    class Meta:
        model = User
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'First name'}),
                'last_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Last name'}),
                }

        fields = ('first_name', 'last_name', 'password')
