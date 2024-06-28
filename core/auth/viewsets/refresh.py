from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    """
    Validates the login credentials and returns the serialized user data along with the
    refresh and access tokens.

    Args:
    - attrs (dict): A dictionary containing the login credentials.

    Returns:
    - dict: A dictionary containing the serialized user data and the refresh and access tokens.
    """
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
