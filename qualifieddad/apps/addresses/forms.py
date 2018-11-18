from django import forms
from django.forms import ModelForm
from apps.addresses.models import Address
from . import models

class AddAddressForm(forms.ModelForm):

    class Meta:
        model = models.Address

        widgets = {'company_name':forms.TextInput(
            attrs={

                'class':'form-control',
                'placeholder':'Company name (optional)...',
                'autocomplete':'section-blue address-level3',
            }
        ),
        #             'street_number':forms.TextInput(
        #     attrs={
        #
        #         'class':'form-control',
        #         'id':'street_number',
        #         'placeholder':'Company name (optional)...',
        #         'autocomplete':'section-blue address-level3',
        #     }
        # ), FOR USA, STREET NUMBER AND NAME ARE IN THE SAME FIELD
                    'address_line1':forms.TextInput(
            attrs={

                'class':'form-control',
                'id':'route',
                'placeholder':'Street address...',
                'autocomplete':'section-blue address-line1'
            }
        ),
                    'city':forms.TextInput(
            attrs={

                'class':'form-control',
                'id':'locality',
                'placeholder':'City...',
                'autocomplete':'section-blue address-level2',
            }
        ),
                    'state':forms.TextInput(
            attrs={

                'class':'form-control',
                'id':'administrative_area_level_1',
                'placeholder':'State...',
                'autocomplete':'section-blue address-level1',
            }
        ),
                    'country':forms.TextInput(
            attrs={

                'class':'form-control',
                'id':'country',
                'placeholder':'Country...',
                'autocomplete':'section-blue country-name',
            }
        ),
                    'postcode':forms.TextInput(
            attrs={

                'class':'form-control',
                'id':'postal_code',
                'placeholder':'Postcode...',
                'autocomplete':'section-blue postal-code'
            }
        ),
        'user':forms.Select(attrs={'class':'form-control',}),
        'full_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name...', 'autocomplete':'section-blue name'}),
        'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number...', 'autocomplete':'section-blue tel'}),
        'additional_instructions':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Provide details such as building description, nearby landmark, or other navigation instructions', 'autocomplete':'section-blue address-level4'}),
        'call_box':forms.TextInput(attrs={'class':'form-control', 'placeholder':'1234'}),
        }
        fields = ('company_name', 'address_line1', 'city', 'state', 'country', 'postcode', 'user',
        'full_name', 'phone', 'additional_instructions', 'call_box',
        )
