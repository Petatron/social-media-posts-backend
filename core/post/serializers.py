from core.abstract.serializer import AbstractSerializer
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PostSerializer(AbstractSerializer):
    """Serializer for the Post model."""
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_liked(self, obj):
        request = self.context.get('request', None)
        if request is None or not request.user.is_anonymous:
            return False

        return request.user.has_liked(obj)

    def get_likes_count(self, obj):
        return obj.liked_by.count()

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True

        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        """Convert the instance to a dictionary."""
        data = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(data['author'])
        data['author'] = UserSerializer(author).data
        return data

    class Meta:
        model = Post
        # List of all the fields that can only be read by the user
        fields = ['id', 'author', 'body', 'edited', 'liked', 'likes_count','created', 'updated']
        read_only_fields = ['edited']
