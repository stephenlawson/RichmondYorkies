from django.forms import ModelForm
from .models import Contact
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark',}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'captcha']