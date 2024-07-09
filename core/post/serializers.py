from core.abstract.serializer import AbstractSerializer
from core.post.models import Post


class PostSerializer(AbstractSerializer):
    # Rewriting some fields like the public id to be represented as the id of the object

    class Meta:
        model = Post
        # List of all the fields that can be included in a request or a response
        fields = ['post_id']
        # # List of all the fields that can only be read by the user
        read_only_field = ['post_id', 'author']
