from rest_framework import authentication
from community.models import CommunityPost, CommunityPost, CommunityPost
from .serializers import (
    CommunityPostSerializer,
    CommunityPostSerializer,
    CommunityPostSerializer,
)
from rest_framework import viewsets


class CommunityPostViewSet(viewsets.ModelViewSet):
    serializer_class = CommunityPostSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CommunityPost.objects.all()
