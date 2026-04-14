from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model  = ContactMessage
        fields = ['name', 'email', 'inquiry_type', 'subject', 'budget', 'timeline', 'message', 'heard_from']
        widgets = {
            'name': forms.TextInput(attrs={
                'class':       'form-input-custom',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class':       'form-input-custom',
                'placeholder': 'you@example.com',
            }),
            'inquiry_type': forms.Select(attrs={
                'class': 'form-input-custom form-select-custom',
            }),
            'subject': forms.TextInput(attrs={
                'class':       'form-input-custom',
                'placeholder': 'Brief description of your need',
            }),
            'budget': forms.Select(attrs={
                'class': 'form-input-custom form-select-custom',
            }),
            'timeline': forms.Select(attrs={
                'class': 'form-input-custom form-select-custom',
            }),
            'message': forms.Textarea(attrs={
                'class':       'form-input-custom form-textarea',
                'placeholder': 'Tell me about your vision, project, or question...',
                'rows':        6,
            }),
            'heard_from': forms.Select(attrs={
                'class': 'form-input-custom form-select-custom',
            }),
        }
        labels = {
            'name':         'Your Name',
            'email':        'Email Address',
            'inquiry_type': 'Type of Inquiry',
            'subject':      'Subject',
            'budget':       'Budget Range',
            'timeline':     'Project Timeline',
            'message':      'Message',
            'heard_from':   'Where Did You Hear About Me?',
        }
