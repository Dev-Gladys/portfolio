from django import forms
from .models import Message
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        strip=True,  # Removes leading and trailing whitespace
    )
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator()]
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        max_length=2000
    )

    def clean(self):
        cleaned_data = super().clean()
        # Additional custom validation if needed
        return cleaned_data

    def clean_message(self):
        message = self.cleaned_data['message']
        # Strip HTML tags
        cleaned_message = strip_tags(message)
        return cleaned_message