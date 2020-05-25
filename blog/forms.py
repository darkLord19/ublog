from django import forms
from django.core.validators import EmailValidator
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'keywords')


class CommentForm(forms.ModelForm):
    author = forms.CharField(
        required=True,
        max_length=15,
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'Ms. Chanandler Bong'}),
    )
    msg = forms.CharField(
        required=True,
        max_length=300,
        label='Comment',
        widget=forms.TextInput(attrs={'placeholder': 'Write your comment here.'}),
    )

    class Meta:
        model = Comment
        fields = ('msg', 'author')


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=25,
        label='Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'Rachel Green', 'class': 'form-control', 'id': 'name'}
        ),
        error_messages={'required': 'Please enter your name.'},
    )
    from_email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'phoebe@smellycat.com',
                'class': 'form-control',
                'id': 'email',
            }
        ),
    )
    msg = forms.CharField(
        required=True,
        max_length=300,
        label='Message',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'What do you want to ask?',
                'class': 'form-control',
                'id': 'message',
                'data-validation-required-message': 'Please enter your message.',
                'rows': '3',
            }
        ),
    )

    fields = ('name', 'from_email', 'msg')
