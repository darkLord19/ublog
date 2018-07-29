from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'body',)

class CommentForm(forms.ModelForm):
    author = forms.CharField(required=True, max_length=15, label='Name', \
                            widget=forms.TextInput(attrs={'placeholder': 'Ms. Chanandler Bong'}))
    msg = forms.CharField(required=True, max_length=300,label='Comment', \
                            widget=forms.TextInput(attrs={'placeholder': 'Write your comment here.'}))
    class Meta:
        model = Comment
        fields = ('author', 'msg')