from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "reddit_app/index.html", {'posts':posts})

def create_post(request):
    user_obj = User.objects.get(pk=1)
    # post_obj = Post.objects.create(
    #                 title="Rainy?",
    #                 text="Is it raining currently in th place you live at?",
    #                 author = user_obj
    #             )
    # print(post_obj.id)
    # print(Post.objects.all()[0].text)
    # print(Post.objects.all())
    # post = Post.objects.get(pk=9)
    # post.comment_set.create(text='im in australia and its very hot here', post=post, author=user_obj)    
    # post.comment_set.create(text='not rainy, there are some clouds though!', post=post, author=user_obj)
    # post.comment_set.create(text='raining all day here at india', post=post, author=user_obj)

    # print(post.comment_set.all())
    return render(request, "reddit_app/index.html", {})

def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post.text)
    comments = post.comment_set.all()
    print(comments)
    return render(request, "reddit_app/single_post.html", {'post':post, 'comments':comments})
