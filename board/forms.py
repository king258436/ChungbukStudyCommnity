from django import forms
from .models import Post, Comment

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'pubDate', 'lectName']

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'pubDate']
