from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    phone = forms.CharField(max_length=20, label='Phone Number')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)