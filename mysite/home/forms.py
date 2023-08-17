from django import forms
from .models import Ssh


# class CreateSshForm(forms.Form):

#     ssh_name = forms.CharField(label='Username', max_length=10, widget=forms.TextInput)
#     password = forms.CharField(label='Password', max_length=5, widget=forms.PasswordInput)
#     pub_date = forms.DateField(widget=forms.DateInput)
#     pub_date.widget = forms.DateInput(attrs={'type': 'date'})
#     password.widget = forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'})


class CreateSshForm(forms.ModelForm):
    """Form definition for CreateSsh."""

    class Meta:
        """Meta definition for CreateSshform."""

        model = Ssh
        widgets = {'ssh_name': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Enter Username'}),
                   'password': forms.PasswordInput({'class': 'password', 'placeholder': 'Enter Password'}),
                   'pub_date': forms.DateInput(attrs={'class': 'date', 'type': 'date'})}
        fields = ['ssh_name', 'password', 'pub_date']
        labels = {'ssh_name': '', 'password': '', 'pub_date': ''}

