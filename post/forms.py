from django import forms
from captcha.fields import ReCaptchaField

from .models import Post, Comment


class PostForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={
        'theme': 'clean',
    })

    class Meta:
        model = Post
        fields = [
            # 'user',
            'title',
            'category',
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'full_name',
            'email_address',
            'content',
        ]
