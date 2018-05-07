from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'accounts'

urlpatterns = [
	path('', login_view, name='login_view'),
	path('register/', register_view, name='register'),
	path('logout/', logout_view, name='logout'),
	path('profile/', profilemy, name='profilemy'),
	path('update/', kabinetedit, name='kabinetedit'),
	path('listusers/', listusers, name='listusers'),
	path('listusers/<int:id>/', userdetail, name='userdetail'),
	path('listusers/<int:id>/chat/', chat, name='chat'),
	path('foto/', photomy, name='photomy'),
	path('allchat/', allchat, name='allchat'),
	path('listusers/<int:id>/foto/', photoyou, name='photoyou'),
	path('photo/<int:id>/', likephoto, name='likephoto'),
	path('api/listusers/<int:id>/foto/like/', PostLikeApiToggle.as_view(), name='like-api-toggle'),

]