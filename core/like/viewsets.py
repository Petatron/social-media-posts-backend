from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from core.post.models import Post
from .models import Like
from .serializers import LikeSerializer
from core.abstract.viewsets import AbstractViewSet
import logging

logger = logging.getLogger(__name__)

class LikeViewSet(AbstractViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'public_id'
    lookup_url_kwarg = 'post_id'  # This matches the URL configuration
    logger.info(f"Enter likeviewset")
    @action(detail=True, methods=['post'])
    def like(self, request, post_id=None):
        logger.info(f"Entering LikeViewSet like action for post_id: {post_id}")
        
        try:
            user = request.user
            logger.info(f"User object: {user}")
            
            if user is None:
                logger.error("User is None. Authentication may have failed.")
                return Response({'detail': 'Authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)
            
            logger.info(f"Like attempt by user {user.public_id} for post {post_id}")
            
            post = Post.objects.get(public_id=post_id)
            logger.info(f"Post {post_id} found")
            
            like = self.create_like(user, post)
            serializer = self.get_serializer(like)
            logger.info(f"Like created successfully for user {user.public_id} and post {post_id}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Post.DoesNotExist:
            logger.warning(f"Post {post_id} not found")
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception(f"Unexpected error in like creation: {str(e)}")
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def create_like(user, post):
        logger.info(f"Attempting to create like for user {user.public_id} and post {post.public_id}")
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            logger.warning(f"Like already exists for user {user.public_id} and post {post.public_id}")
            raise ValueError("Post is already liked by this user.")
        logger.info(f"Like created successfully: {like.id}")
        return like