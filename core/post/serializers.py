from core.abstract.serializer import AbstractSerializer
from core.post.models import Post


class PostSerializer(AbstractSerializer):
    # Rewriting some fields like the public id to be represented as the id of the object

    class Meta:
        model = Post
        # List of all the fields that can be included in a request or a response
        fields = ['post_id']
        # List of all the fields that can only be read by the user
        read_only_fields = ['post_id', 'author']

        def is_authorized_user(self, user: str):
            '''
            param user: the user authorized to perform the action, used to compared with the post author
            '''
            # logic here to check if the post author is the authorized user
            return self.model.author == user
