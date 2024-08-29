from django.db import models
from core.abstract.models import AbstractModel, AbstractManager

class LikeManager(AbstractManager):
    pass

class Like(AbstractModel):
    user = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(to="core_post.Post", on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        db_table = 'core_like'

    def __str__(self):
        return f"{self.user.email} liked {self.post.id} at {self.created_at}"