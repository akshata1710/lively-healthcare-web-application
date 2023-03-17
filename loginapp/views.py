from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from random import randrange
from .models import Todo

# Create your views here.


def hom(request):
	if request.user.is_authenticated:
		log_user = request.user
		data = Todo.objects.filter(user=log_user)
		return render(request, "hom.html", {"data": data})
	else:
		return render(request, "user_login.html")


def create(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			task = request.POST.get("Task")
			data = Todo(text=task, user=request.user)
			data.save()
			return render(request, "create.html", {"msg": "we will get back to you"})
		else:
			return render(request, "create.html",)
	else:
		return redirect("user_login")


def user_signup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			try:
				usr = User.objects.get(username=un)
				return render(request, "user_signup.html", {"msg": "user already exists"})
			except User.DoesNotExist:
				usr = User.objects.create_user(username=un, password=pw1)
				usr.save()
				return redirect("user_login")
		else:
			return render(request, "user_signup.html", {"msg": "passwords didnot match"})
	else:
		return render(request, "user_signup.html")


def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un1")
		pw = request.POST.get("pass1")
		usr = authenticate(username=un, password=pw)
		if usr is None:
			return render(request, "user_login.html", {"msg": "invalid login"})
		else:
			login(request, usr)
			return redirect('hom')

	else:
		return render(request, "user_login.html")


def user_logout(request):
	logout(request)
	return redirect("user_login")


def user_np(request):
	if request.method == "POST":
		un = request.POST.get("username")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			usr = User.objects.get(username=un)
			usr.set_password(pw1)
			usr.save()
			return redirect("user_login")
		else:
			return render(request, "user_np.html", {"msg": "passwords did not match"})

	else:
		return render(request, "user_np.html")


def delete(request, id):
	d = Todo.objects.get(id=id)
	d.delete()
	return redirect("hom")
