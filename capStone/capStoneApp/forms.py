from django import forms
from .models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
class CreateCardForm(forms.ModelForm):
    class Meta:
        model = CreateCard
        fields = "__all__"