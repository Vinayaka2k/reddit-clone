from django.urls import path
from . import views

app_name = "reddit_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create-post/", views.create_post, name="create_post"),
    path("trending/", views.create_post, name="trending"),
    path("post/<int:post_id>/", views.single_post, name="single_post")
]