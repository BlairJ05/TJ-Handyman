from django import forms
from .models import *


class ReviewForm(forms.Form):
    review_text = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField()


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = CreateCard
        fields = "__all__"
