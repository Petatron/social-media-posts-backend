from rest_framework import routers
from core.auth.viewsets import RegisterViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet
from core.auth.viewsets import RefreshViewSet
from core.post.viewsets import PostViewSet
from core.like.viewsets import LikeViewSet
from django.urls import path, include

router = routers.SimpleRouter()


router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
    path('like/<str:post_id>/', LikeViewSet.as_view({'post': 'like'}), name='like-post'),
]