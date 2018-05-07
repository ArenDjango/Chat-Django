from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect


from django.views.generic import RedirectView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


# Create your views here.


def landing(request):
	return render(request, "accounts/login.html", locals())