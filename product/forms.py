from django import forms


class SearchBarForm(forms.Form):
    name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "col-lg-8 col-md-8"
            }
        )
    )