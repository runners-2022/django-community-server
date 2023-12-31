# Django
from django.core.management.base import BaseCommand

# Models
from community.apps.rankings.models import RankingGroup


# Main Section
class Command(BaseCommand):
    help = 'Create Ranking Group Community Hourly'

    def handle(self, *args, **kwargs):
        RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='LIVE')
