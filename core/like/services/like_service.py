from core.user.models import User
from core.post.models import Post
from core.like.models import Like

class LikeService:
    @staticmethod
    def like(user: User, post: Post):
        if post is None:
            raise ValueError("Post cannot be null.")
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            raise ValueError("Post is already liked by this user.")
        return like

    @staticmethod
    def remove_like(user: User, post: Post):
        if post is None:
            raise ValueError("Post cannot be null.")
        Like.objects.filter(user=user, post=post).delete()

    @staticmethod
    def has_liked(user: User, post: Post) -> bool:
        if post is None:
            return False
        return Like.objects.filter(user=user, post=post).exists()
