from django import forms
from django.contrib.auth import authenticate

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Introduce tu usuario",
                "class": "form-control",
                "autofocus": True,
            },
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Introduce tu contraseña",
                "class": "form-control",
            }
        ),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos del usuario no son correctos")

        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Introduce tu contraseña",
                "class": "form-control",
            }
        ),
    )
    password_confirm = forms.CharField(
        label="Repetir contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirma tu contraseña",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Introduce tu usuario",
                    "class": "form-control",
                    "autofocus": True,
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Introduce tu correo",
                    "class": "form-control",
                    "autofocus": True,
                },
            ),
        }

    def valid_password(self):
        if self.cleaned_data["password"].length() <= 5:
            self.add_error("password", "La contraseña debe tener más de 5 caracteres")

    def clean_password_confirm(self):
        if self.cleaned_data["password"] != self.cleaned_data["password_confirm"]:
            self.add_error("password_confirm", "Las contraseñas deben ser iguales")


class VerificationForm(forms.Form):
    codregistro = forms.CharField(
        label="Código de verificación",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "introduzca su código de verificación",
                "class": "form-control",
            }
        ),
    )

    def __init__(self, id_user, *args, **kwargs):
        self.id_user = id_user
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        codigo = self.cleaned_data["codregistro"]

        if len(codigo) == 6:
            # Verificando si el código y el id del usuario son válidos
            activo = User.objects.code_validation(self.id_user, codigo)
            if not activo:
                raise forms.ValidationError("El código es incorrecto")
        else:
            raise forms.ValidationError("El código es incorrecto")
