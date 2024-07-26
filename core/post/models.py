# Description: This file contains the model for the Post object.
from django.db import models

from core.abstract.models import AbstractModel, AbstractManager


class PostManager(AbstractManager):
    def create_post(self, title, author, body, **kwargs):
        """Constructor for a social media post with a title, author, and body."""
        if title is None:
            raise ValueError('Post must have a title.')
        if author is None:
            raise ValueError('Post must have an author.')
        if body is None:
            raise ValueError('Post must have a body.')

        return {
            "title": title,
            "author": author,
            "body": body,
        }


class Post(AbstractModel):
    author = models.TextField()
    # author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)     # TODO: make connection to User model
    title = models.CharField(max_length=255)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return f"{self.author.name}"

    class Meta:
        db_table = "'core.post'"
