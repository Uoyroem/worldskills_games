from django import forms

from . import models


class GameCreationForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = ['title', 'slug', 'description', 'script', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'script': forms.FileInput(attrs={'class': 'form-control-file'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
