from django import forms

from .models import Review


class ReviewForem(forms.Form):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'text': forms.TextInput(attrs={'class': 'input'}),
        }
