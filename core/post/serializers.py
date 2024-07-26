from core.abstract.serializer import AbstractSerializer
from core.post.models import Post

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PostSerializer(AbstractSerializer):
    """Serializer for the Post model."""
    class Meta:
        model = Post
        # List of all the fields that can only be read by the user
        fields = ['id', 'title', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['edited']
 
    def check_author(self, value): # TODO: this should be validate_author
        """Validate if the author of the post is the same as the user logged in."""
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value
    
    def create(self, validated_data):
        # Use the `create_post` method in models.PostManager to create a new post.
        return Post.objects.create_post(**validated_data)
