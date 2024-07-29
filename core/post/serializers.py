from core.abstract.serializer import AbstractSerializer
from core.post.models import Post

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PostSerializer(AbstractSerializer):
    """Serializer for the Post model."""
    author = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    class Meta:
        model = Post
        # List of all the fields that can only be read by the user
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['edited']
