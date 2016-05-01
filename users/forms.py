from django import forms
from django.contrib.auth import (
login,
logout,
get_user_model,
authenticate
)

User = get_user_model()

class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Name incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Password incorrect')
        return super(LoginUserForm, self).clean()
class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField()
    confirmed_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmed_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'confirmed_email','password', 'confirmed_password']
    def clean_confirmed_email(self):
        email = self.cleaned_data.get('email')
        confirmed_email = self.cleaned_data.get('confirmed_email')
        if email != confirmed_email:
            raise forms.ValidationError('Email must match')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email
    def clean_confirmed_password(self):
        password = self.cleaned_data.get('password')
        confirmed_password = self.cleaned_data.get('confirmed_password')
        if password != confirmed_password:
            raise forms.ValidationError('Password must match')
        return password


