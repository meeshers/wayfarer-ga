from django.forms import ModelForm


class LoginForm(forms.Form):
    login_form = forms.Charfield(label="Login Form", max_length=100)
