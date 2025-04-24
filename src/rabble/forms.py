from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_body']
        labels = {
            'post_title': 'Title',
            'post_body': 'Content'
        }