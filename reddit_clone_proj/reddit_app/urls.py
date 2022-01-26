from django.urls import path
from . import views

app_name = "reddit_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create-post/", views.create_post, name="create_post"),
    path("trending/", views.create_post, name="trending"),
    path("post/<int:post_id>/", views.single_post, name="single_post"),
    path("post/<int:post_id>/comment", views.comment, name="comment"),
    path("profile/", views.profile, name="profile"),
    path("post/<int:post_id>/delete", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/update_helper", views.update_post_helper, name="update_post_helper"),
    path("post/<int:post_id>/update", views.update_post, name="update_post")
]