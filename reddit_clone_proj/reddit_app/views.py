from django.shortcuts import render, get_object_or_404, redirect

import reddit_app
from .models import Post, Comment, Vote
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "reddit_app/index.html", {'posts':posts})

def create_post(request):
    user_obj = User.objects.get(pk=1)
    post_obj = Post.objects.create(
                    title="Fav TV Show?",
                    text="List your TV SHow here",
                    author = user_obj
                )
    print(Post.objects.all())
    post = Post.objects.get(pk=11)
    post.comment_set.create(text='Friends', post=post, author=user_obj)    
    post.comment_set.create(text='Others', post=post, author=user_obj)
    post.comment_set.create(text='I dont watch TV  ', post=post, author=user_obj)

    # print(post.comment_set.all())
    return render(request, "reddit_app/index.html", {})

def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # print(post.text)
    comments = post.comment_set.all()
    # print(comments)
    return render(request, "reddit_app/single_post.html", {'post':post, 'comments':comments})

def comment(request, post_id):
    if request.method == "POST":
        comment_text = request.POST["comment_text"]
        user_obj = User.objects.get(pk=1)
        post = Post.objects.get(pk=post_id)
        post.comment_set.create(text=comment_text, post=post, author=user_obj)    
    return redirect("reddit_app:single_post", post_id=post_id) 
    
def profile(request):
    user_obj = User.objects.get(pk=1)
    posts = Post.objects.filter(author=user_obj)
    # votes = Vote.objects.filter(user=user_obj).values()
    vote_list = []
    for post in posts:
        try:
            vote = Vote.objects.get(user=user_obj, post=post).vote_type
        except Vote.DoesNotExist:
            vote = None
        vote_list.append(vote)
    posts = zip(posts, vote_list)
    return render(request, 'reddit_app/profile.html', {'posts':posts, 'user':user_obj})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("reddit_app:profile") 

def update_post_helper(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'reddit_app/update_post.html', {'post':post})

def update_post(request, post_id):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        Post.objects.filter(pk=post_id).update(title=title, text=text)
    return redirect("reddit_app:profile")

def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = User.objects.get(pk=1)
    res = post.upvote(user)
    # print(res)
    # print(post.votes)
    # print(Vote.objects.all().values())
    # print(Vote.objects.all().delete())
    return redirect("reddit_app:profile")

def downvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = User.objects.get(pk=1)
    res = post.downvote(user)
    # print(res)
    # print(post.votes)
    # print(Vote.objects.all().values())
    # print(post.vote_set.values())
    return redirect("reddit_app:profile")