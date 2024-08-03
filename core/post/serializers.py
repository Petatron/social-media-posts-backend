from core.abstract.serializer import AbstractSerializer
from core.post.models import Post
from core.user.models import User

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PostSerializer(AbstractSerializer):
    """Serializer for the Post model."""
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    def to_representation(self, instance):
        """Convert the instance to a dictionary."""
        data = super().to_representation(instance)
        data["author_uid"] = instance.author.public_id
        return data

    class Meta:
        model = Post
        # List of all the fields that can only be read by the user
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['edited']
