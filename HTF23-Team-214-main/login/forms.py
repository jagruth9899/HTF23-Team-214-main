# # myapp/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser

# class LoginForm(AuthenticationForm):
#     pass

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')
# myapp/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
# from django.contrib.auth.forms import AuthenticationForm

# class LoginForm(AuthenticationForm):
#     pass

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')

# class CustomSignUpForm(UserCreationForm):
#     username = forms.CharField(
#         max_length=150,
#         help_text='',  # Remove the default help text
#         error_messages={
#             'required': 'Custom username field is required.',
#         }
#     )
    
#     email = forms.EmailField(
#         max_length=254,
#         help_text='Enter a valid email address.',
#         error_messages={
#             'required': 'Custom email field is required.',
#             'invalid': 'Enter a valid email address.',
#         }
#     )

#     password1 = forms.CharField(
#         max_length=128,
#         help_text='Your password must contain at least 8 characters.',
#         widget=forms.PasswordInput,
#         error_messages={
#             'required': 'Custom password field is required.',
#         }
#     )

#     password2 = forms.CharField(
#         max_length=128,
#         help_text='Enter the same password as above, for verification.',
#         widget=forms.PasswordInput,
#         error_messages={
#             'required': 'Custom password confirmation field is required.',
#         }
#     )

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class LoginForm(AuthenticationForm):
    pass

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomSignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        error_messages={
            'required': 'Custom username field is required.',
        }
    )
    
    email = forms.EmailField(
        max_length=254,
        error_messages={
            'required': 'Custom email field is required.',
            'invalid': 'Enter a valid email address.',
        }
    )

    password1 = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Custom password field is required.',
        }
    )

    password2 = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Custom password confirmation field is required.',
        }
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


