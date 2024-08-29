from core.abstract.serializer import AbstractSerializer
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PostSerializer(AbstractSerializer):
    """Serializer for the Post model."""
    author = serializers.SlugRelatedField(queryset=User.objects.all(), 
                                          slug_field='public_id', required=False)  # author is optional
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)

    def create(self, validated_data):
        # Automatically set the author to the currently authenticated user if not provided
        if 'author' not in validated_data:
            validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

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
        fields = ['id', 'author', 'title', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['edited']
