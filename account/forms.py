from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("Oops! this email is already registered!. Try different one.")
		return email

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError("Passwords don't match.")
		return cd['password2']

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])

		user.is_active = False

		if commit:
			user.save()
			
			Profile(user=user).save()
			
			user.profile.send_activation_email()

		return user


