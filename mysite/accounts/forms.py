from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)
    # email = forms.EmailField(required=False)


