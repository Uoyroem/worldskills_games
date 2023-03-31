from django import forms

from . import models


class GameCreationForm(forms.ModelForm):
    github_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Game
        fields = ['title', 'slug', 'description', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
