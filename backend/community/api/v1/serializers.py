from rest_framework import serializers
from community.models import CommunityPost, CommunityPost


class CommunityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPost
        fields = "__all__"
