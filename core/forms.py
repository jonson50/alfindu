from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg',
               'placeholder': 'Correo electronico'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg',
               'placeholder': 'Contraseña'}
    ))
