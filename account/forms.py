import re

from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email


class ManagerUserInviteForm(forms.Form):
    email_list = forms.CharField(help_text='Enter a Comma or Semicolon Seperated List of Email Addresses',
        widget=forms.Textarea)

    def clean_email_list(self):
        SEPARATOR_RE = re.compile(r'[,;]+')
        emails = [x.strip() for x in SEPARATOR_RE.split(self.cleaned_data['email_list'])]
        validated_emails = []
        new_emails = []
        for email in emails:
            try:
                validate_email(email)
            except forms.ValidationError:
                continue
            validated_emails.append(email)
        existing_emails = User.objects.all().values_list('email', flat=True)
        new_emails = set(validated_emails) - set(existing_emails)
        if not new_emails:
            raise forms.ValidationError('Please supply valid emails')
        return new_emails
