from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
attrs={'class': 'form-control'}


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs),

    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs),
    )



class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs=attrs))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs=attrs))

    username = forms.CharField( label='Username', widget=forms.TextInput(attrs=attrs),)

    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs=attrs),)

    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs=attrs),)

    password2 = forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs=attrs),)


    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
        }

