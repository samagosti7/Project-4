from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
# Form for post submission
    class Meta: 
        model = Post
        fields = ['title', 'content']
        # widgets = {
        #     'content': SummernoteWidget(),
        # }


