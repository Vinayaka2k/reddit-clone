from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth.models import User

def index(request):
    
    return render(request, "reddit_app/index.html", {})

def create_post(request):
    # user_obj = User.objects.get(pk=1)
    # post_obj = Post.objects.create(
    #                 title="Your Fav Movie?",
    #                 text="Please comment your favourite movie watched preferably in Action/Drama genre",
    #                 author = user_obj
    #             )
    # print(post_obj.id)
    # print(Post.objects.all())
    return render(request, "reddit_app/index.html", {})
