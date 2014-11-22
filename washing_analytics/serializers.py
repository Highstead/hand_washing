from rest_framework import serializers
from models import TeamReduce


class TeamReduceSerializer(serializers.ModelSerializer):

    class Team:
        model = TeamReduce
        fields = ('id', 'team', 'division', 'complete', 'unwashed', 'timespent')
