from django import forms
# from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial


class PostForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        fields = ('tutorial_title', 'tutorial_content', 'tutorial_published')
        # widgets = {
        #     'name': TinyMCE(attrs={'cols': 80, 'rows': 50, 'class': 'form-control'})
        # }
        # text = forms.CharField(widget=TinyMCE(
        #     attrs={'cols': 80, 'rows': 50, 'class': 'form-control'}))
