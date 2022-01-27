from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login as sess_login, logout as sess_logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

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
    sess_logout(request)
    return redirect("reddit_app:index")
    
# def delete(request):
#     return render(request, "user_app/login.html", {})

# def update_password(request):
#     return render(request, "user_app/login.html", {})

# def request_reset_password(request):
#     return render(request, "user_app/login.html", {})

# def reset_password(request):
#     return render(request, "user_app/login.html", {})