from django import forms

from django.contrib import messages

import json
import urllib

from pagedown.widgets import AdminPagedownWidget

from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

from .models import *

User = get_user_model()

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        exclude = [""]

class UserLoginForm(forms.Form):
	username = forms.CharField(label='')
	password = forms.CharField(label='', widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Пользователь не сушетсвует!")
			if not user.check_password(password):
				raise forms.ValidationError("Не правильный пароль")
			if not user.is_active:
				raise forms.ValidationError("Пользователь забанен")
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(label='')
	email = forms.CharField(label='')
	password = forms.CharField(label='')
	first_name = forms.CharField(label='')
	last_name = forms.CharField(label='')

	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'email',
			'username',
			'password',
		]


	def clean_email(self):
		email = self.cleaned_data.get('email')

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Емайл уже сушествует")
		return email


class Createimg(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			"avatar",
		]

class Editprofile(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			"avatar",
			"placework",
			"city"
		]

class MessageForm(forms.ModelForm):
	# content = forms.CharField(widget=AdminPagedownWidget)
	class Meta:
		model = Chat
		fields = [
			"message",
			"useryou"
		]

class AddPhoto(forms.ModelForm):
	# content = forms.CharField(widget=AdminPagedownWidget)
	class Meta:
		model = Photo
		fields = [
			"imageuser",
			"orphotoorvideo"
		]