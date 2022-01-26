from enum import unique
from sqlite3 import IntegrityError
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def upvote(self, user):
        try:
            self.vote_set.create(user=user, post=self, vote_type=True)
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'already_upvoted'
        return 'ok'

    def downvote(self, user):
        try:
            self.vote_set.create(user=user, post=self, vote_type=False)
            self.votes -= 1
            self.save()
        except IntegrityError:
            return 'already_downvoted'
        return 'ok'

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_type = models.BooleanField()

    class Meta:
        unique_together = ('user', 'post',)