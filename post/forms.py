from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms
from captcha.fields import ReCaptchaField

from .models import Post, Comment


class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()

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

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Field('full_name', wrapper_class='col-md-6'),
                Field('email_address', wrapper_class='col-md-6')
            ),
            Row(
                Field('content', wrapper_class='col-md-12', rows=4)
            ),
            Row(
                Field('captcha', wrapper_class='col-md-12')
            )
        )

    class Meta:
        model = Comment
        fields = [
            'full_name',
            'email_address',
            'content',
        ]
