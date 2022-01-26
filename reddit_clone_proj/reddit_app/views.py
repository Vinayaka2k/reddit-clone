from django.shortcuts import render

def index(request):
    return render(request, "reddit_app/index.html", {})