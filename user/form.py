from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


def help_password():
    text = ("Votre mot de passe ne doit pas être trop similaire à vos autres informations personnelles.",
            "Votre mot de passe doit contenir au moins 8 caractères.",
            "Votre mot de passe ne doit pas être un mot de passe couramment utilisé.",
            "Votre mot de passe ne doit pas être entièrement numérique.")

    help_list = '<ul>{}</ul>'.format("".join('<li>{}</li>'.format(help_text) for help_text in text))
    return help_list


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=help_password(),
    )
    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Entrez le même mot de passe.",
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'username']
        labels = {
            'email': "Email",
            "username": "Nom d'utilisateur",
            "password": "Mot de passe"
        }


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ['order_by_1', 'order_by_2', 'order_by_3', 'order_by_4']
        labels = {
            'order_by_1': "ordre 1",
            'order_by_2': "ordre 2",
            'order_by_3': "ordre 3",
            'order_by_4': "ordre 4",
        }
