from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from PIL import Image
from .models import *
from .forms import *

import cv2
import datetime
import numpy as np

# Create your views here.

def post_comments(request):
    if request.method== "POST":
        if request.user.is_authenticated:
            form = CommentsForm({'comment':request.POST['text'], 'username':request.user.username, 'date':datetime.datetime.now()})
            if form.is_valid():
                contents = form.cleaned_data['comment']
                username = form.cleaned_data['username']
                date     = form.cleaned_data['date']
                cmt      = Comments.objects.create(text=contents, posted_by=username, time_posted=date)
                return render(request, 'index.html', {'comments': cmt, 'username': cmt.username, 'form': CommentsForm})
            else:
                messages.error(request, "form is not valid")
                return render(request, 'index.html', {'form': CommentsForm})
        else:
            messages.info(request, "You're not logged in to your account")
            return render(request, 'index.html')
    else:
        return render(request, "index.html")

def send_image(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            username = request.user.username
            img = request.FILES["image"]
            img_ins = Profile_Picture.objects.create(file_name=username, image=img)
            img = Profile_Picture.objects.filter(file_name=username)
            img = Image.open(img)
            return render(request, "index.html", {"image": img})


def homepage(request):
	return render(request, 'index.html', {'form': CommentsForm})

def login_page(request):
	return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html', {'form': CommentsForm})
        else:
            messages.info(request, "invalid credencials")
            return render(request, "login.html")
    else:
            return render(request, 'index.html', {'form': CommentsForm})

def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect("register")
        elif password1 != password2:
            messages.info(request, "password not matching")
            return redirect("register")
        else:
            print(request.POST)
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            auth.login(request, user)
            messages.info(request, "user created")
            return render(request, 'index.html', {'form': CommentsForm})
    else:
        return render(request, 'registration.html')