from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=100, label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label=_('Password Repeat'), widget=forms.PasswordInput)
    captcha = ReCaptchaField(label=_('Captcha'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_('Passwords do not match.'))
        else:
            raise forms.ValidationError(_('Missing password field(s).'))

        return password2


class EditProfileForm(forms.ModelForm):
    captcha = ReCaptchaField(label=_('Captcha'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
