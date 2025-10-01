from django import forms

class JobApplicationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    phone = forms.CharField(max_length=15, label="Phone Number")
    resume = forms.FileField(label="Upload Resume")
    cover_letter = forms.CharField(widget=forms.Textarea, label="Cover Letter")
from django import forms
from .models import Application

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'resume', 'cover_letter']