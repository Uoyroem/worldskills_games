from django import forms

from . import models


class GameCreationForm(forms.ModelForm):

    class Meta:
        model = models.Game
        fields = ['title', 'slug', 'description', 'game_zip', 'script', 'thumbnail', 'html']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'game_zip': forms.FileInput(attrs={'class': 'form-control'}),
            'script': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.TextInput(attrs={'class': 'form-control'}),
            'html': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
