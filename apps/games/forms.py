from django import forms

from . import models


class GameForm(forms.ModelForm):

    class Meta:
        model = models.Game
        fields = ['title', 'slug', 'description', 'game_zip', 'extracting_script', 'thumbnail', 'html']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'game_zip': forms.FileInput(attrs={'class': 'form-control'}),
            'extracting_script': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.TextInput(attrs={'class': 'form-control'}),
            'html': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class GameResultForm(forms.ModelForm):
    class Meta:
        model = models.GameResult
        fields = ['points']
        widgets = {
            'points': forms.NumberInput(attrs={'hidden': True})
        }

