from django import forms
from django.contrib.auth.models import User
from .models import Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordResetForm, SetPasswordForm


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            "message"
        ]
        widgets = {
            'message': forms.Textarea(attrs={
                "name": "message",
                "id": "message",
                "rows": "10",
                "class": "oleez-textarea",
                "required": "",
            })
        }

class UserCreateForm(UserCreationForm):
    """
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given 
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'id': 'confirmPassword2',
            'required': 'true',
            }
        ),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        ),
    }


class UserLoginForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with no privileges, from the given 
    username and password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        )
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'inputEmail3MD',
                'aria-describedby': 'emailHelpId',
                'placeholder': 'Email Address'
            }
        )
    )


class UserPasswordResetConfirmForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetConfirmForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
