# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect 
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.contrib import auth
from .models import Quote
from django.template.context_processors import csrf

def index(request):
	quotes = Quote.objects.all()
	args = []
	for i in quotes:
		args.append(i.info())
	args.sort()
	return render(request, 'index.html', {"quotes":args})

def login(request):
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			return render(requset, 'index.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def add(request):
	if request.POST:
		author = request.POST.get('author', '')
		text = request.POST.get('text', '')
		u = Quote()
		u.author = author
		u.text = text
		u.save()
	return redirect('/')
