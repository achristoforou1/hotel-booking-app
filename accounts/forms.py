from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    """
    Custom signup form to adjust HTML attributes for validation and styling.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'color: black;'
            field.widget.attrs['required'] = 'required'
