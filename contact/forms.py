from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Field, Layout
from captcha.fields import ReCaptchaField

from .models import Message


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(label=_('Captcha'))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Field('first_name', wrapper_class='col-md-6'),
                Field('last_name', wrapper_class='col-md-6')
            ),
            Row(
                Field('email_address', wrapper_class='col-md-12')
            ),
            Row(
                Field('subject', wrapper_class='col-md-12')
            ),
            Row(
                Field('message', wrapper_class='col-md-12', rows=4, )
            ),
            Row(
                Field('captcha', wrapper_class='col-md-12')
            )
        )

    class Meta:
        model = Message
        fields = [
            'first_name',
            'last_name',
            'email_address',
            'subject',
            'message',
        ]
