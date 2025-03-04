from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from app import services

""" #AUX FUNCTIONS

def create_user (first_name, last_name, username, email, password):
    new_user = User.objects.create_user(username, email, password)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()

    return ("Ok")"""

def home (request):
    return render (request, 'index.html')

def login (request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = services.authentication(username, password)
        if (user):
            request.session['id'] = user.id
            request.session['name'] = username
            return redirect('/app/1')
        else:
            print("Error, not authenticated")
    return HttpResponseRedirect ("/")    


def singup (request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        services.create_user (first_name, last_name, username, email, password)

        return HttpResponseRedirect("/")

    return render (request, 'singup.html', )