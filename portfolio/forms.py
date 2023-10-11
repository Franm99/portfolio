from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100, required=True)
    subject = forms.CharField(label="Subject", max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    