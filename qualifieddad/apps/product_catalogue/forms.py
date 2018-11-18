from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from apps.product_catalogue.models import Review, ReviewHelpfulness
from . import models

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'detail', 'user', 'product', 'rating', 'help', 'verified')

class ReviewHelpfulnessForm(forms.ModelForm):

    class Meta:
        model = ReviewHelpfulness
        fields = ('helpful', 'review', 'user')
