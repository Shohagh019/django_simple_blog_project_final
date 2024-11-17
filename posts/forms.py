from django import forms
from .models import Post
class postForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
