# Django Rest Framework
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class CommunityRetrieveSerializer(ModelSerializer):
    boards = serializers.JSONField(source='board_data')
    posts = serializers.JSONField(source='posts_data')
    banner_medias = serializers.JSONField(source='banner_medias_data')
    is_manager = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ('id', 'title', 'is_manager', 'banner_medias', 'posts', 'boards')

    def get_is_manager(self, obj):
        request = self.context.get('request', None)
        if not request:
            return None
        user = request.user
        if not user.id:
            return None
        community_user = obj.community_users.filter(user=user, is_active=True).first()
        if not community_user:
            return True
        return False
