from core.abstract.serializer import AbstractSerializer
from rest_framework import serializers
from core.user.models import User
from core.post.models import Post
from .models import Like
import logging

logger = logging.getLogger(__name__)
class LikeSerializer(AbstractSerializer):
    user = serializers.SlugRelatedField(
        slug_field='public_id',
        read_only=True  # Set as read-only since it's provided by the viewset
    )
    post = serializers.SlugRelatedField(
        slug_field='public_id',
        read_only=True  # Set as read-only since it's provided by the viewset
    )
    # logger.info(f"Entering like_serializer for post_id: {post.id}")
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['created_at']
