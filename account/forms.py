from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Şifre', widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid username or password')
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=100, label='Şifre', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Şifre Tekrar', widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Şifreler uyuşmuyor')
        else:
            raise forms.ValidationError('Şifreler gönderilmedi')

        return password2
