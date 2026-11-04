
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib.auth.models import User

from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'company_name',
            'job_role',
            'location',
            'salary',
            'job_link',
            'status',
            'applied_date',
            'interview_date',
            'job_description',
            'notes',
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),
            'job_role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job role'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city or Remote'
            }),
            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 6 LPA'
            }),
            'job_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Paste job application URL'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'applied_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'interview_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'job_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter job responsibilities and requirements'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add your personal notes'
            }),
        }


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label='Email ID',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a username'
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password'
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'An account with this email address already exists.'
            )

        return email


class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(
        label='Email ID',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your registered email',
            'autofocus': True
        })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

    def clean(self):
        email = self.cleaned_data.get('username')

        if email:
            user = User.objects.filter(
                email__iexact=email
            ).first()

            if user:
                self.cleaned_data['username'] = user.username
            else:
                self.cleaned_data['username'] = email

        return super().clean()
