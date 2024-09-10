from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'password', 'contact', 'hospitalname', 'branchaddress', 'subject', 'design']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if Register.objects.filter(password=password).exists():
            raise forms.ValidationError("This password is already in use.")
        return password

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if Register.objects.filter(contact=contact).exists():
            raise forms.ValidationError("This contact number is already registered.")
        return contact
