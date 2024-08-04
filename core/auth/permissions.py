from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    """
    The anonymous user: This user has no account on the API and can’t really be identified.
    The registered and active user: This user has an account on the API and can easily perform some actions.
    The admin user: This user has all rights and privileges.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ["post"]:
            return bool(request.user and request.user.is_authenticated)

        return False

    def has_permission(self, request, view):
        if view.basename in ["post"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS

            return bool(request.user and request.user.is_authenticated)

        return False
