from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from markdown_deux import markdown

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

User = get_user_model()

class Photo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
	 							on_delete=models.CASCADE)
	imageuser = models.FileField(upload_to='imageinst', 
						verbose_name='photouser')
	dataimg = models.DateTimeField(auto_now=True, 
									auto_now_add=False)
	photolike = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')

	orphotoorvideo = models.BooleanField(default=False)

	def __unicode__(self):
		return self.imageuser


class Chat(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
	 on_delete=models.CASCADE)
	useryou = models.ForeignKey(settings.AUTH_USER_MODEL,
	 on_delete=models.CASCADE,
	 related_name="useryou")
	message = models.TextField()
	datamessage = models.DateTimeField(auto_now=True, 
									auto_now_add=False)


	def __str__(self):
		return str(self.user)

	def get_like_url_photo(self):
		return reverse("listusers:likephoto", kwargs={"id": self.id})


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='imageusers', verbose_name='Изображение')
	placework = models.TextField(default='Отсутствует')
	city = models.TextField(default='Отсутствует')
	friends = models.ManyToManyField(User, 
				related_name='is_friends',
				blank=True)

	followers = models.ManyToManyField(User, 
				related_name='is_following',
				blank=True)
	zayavkadruzya = models.ManyToManyField(User, 
			related_name='addingfriend',
			blank=True,)

	messagedo = models.ManyToManyField(User, 
				related_name='messagedo',
				blank=True)
	allmessagesstory = models.ManyToManyField(User, 
				related_name='allmessagesstory',
				blank=True)

	last_activity = models.DateTimeField(auto_now=True, 
				auto_now_add=False)




	def __unicode__(self):
		return self.user

	def user_get_absolute_url(self):
		return reverse("accounts:userdetail", kwargs={"id": self.id})


	def get_like_url(self):
		return reverse("foto:like-toggle", kwargs={"id": self.id})

	def get_api_like_url(self):
		return reverse("foto:like-api-toggle", kwargs={"id": self.id})



class Meta:
	verbose_name = 'Профиль'
