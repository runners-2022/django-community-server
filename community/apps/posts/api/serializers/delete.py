# Django Rest Framework
from rest_framework import serializers

# Models
from community.apps.posts.models.index import Post

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostDeleteSerializer(ModelSerializer):
    post_id = serializers.IntegerField(source='id')
    community_id = serializers.IntegerField(source='community.id')

    class Meta:
        model = Post
        fields = ('post_id', 'community_id')
