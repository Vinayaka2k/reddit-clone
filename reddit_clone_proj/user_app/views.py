from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login as sess_login, logout as sess_logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
import requests

def signup(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("reddit_app:index")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        email = request.POST["email"]

        if password == confirm_password:
            try:
                user = User.objects.create_user(username, email, password)
                sess_login(request, user)
                return redirect("reddit_app:index")
            except IntegrityError:
                context = { "error": "Username or email already taken, please try again" }
        else:
            context = {"error" : "Passwords dont match, please try again"}
    return render(request, "user_app/signup.html", context)

def login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("reddit_app:index")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            sess_login(request, user)
            return redirect("reddit_app:index")
        else:
            context = {"error" : "Invalid Username and Password Combination"}
    return render(request, "user_app/login.html", context)


# def signin(request):
#     return render(request, "user_app/login.html", {})

# def settings(request):
#     return render(request, "user_app/login.html", {})

def logout(request):
    # print(User.objects.all())
    sess_logout(request)
    return redirect("reddit_app:index")

# def delete(request):
#     return render(request, "user_app/login.html", {})

# def update_password(request):
#     return render(request, "user_app/login.html", {})

def request_reset_password(request):
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        is_email_valid = User.objects.filter(email=email).exists()
        if is_email_valid:
            # context = { "message" : "An email with directions to reset your password has been sent to you! "}
            requests.post("http://127.0.0.1:8000/api/password_reset/",data={"email":email})
            return redirect("user_app:reset_password")
        else:
            context = { "message" : "This email doesnot exist in the Database" }
    return render(request, "user_app/request-reset-password.html", context)

def reset_password(request):
    if request.method == "POST":
        token = request.POST["token"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            requests.post("http://127.0.0.1:8000/api/password_reset/confirm/",data={"password":password, "token":token})
            return redirect("user_app:login")
        else:
            return render(request, "user_app/reset_password.html", {"error":"Passwords dont match"})
    return render(request, "user_app/reset_password.html", {})