from django import forms
from django_powcaptcha.forms import PowCaptchaForm


class FormWithCaptcha(PowCaptchaForm):
    name = forms.CharField(label="Your name", max_length=100)
