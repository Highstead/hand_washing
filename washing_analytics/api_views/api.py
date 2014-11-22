from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework import status, generics
from rest_framework.response import Response

from washing_analytics.models import TeamReduce
from washing_analytics.serializers import TeamReduceSerializer


class WashHandsData(ListCreateAPIView):


    def post(self, request, *args, **kwargs):

        return Response({}, status=status.HTTP_201_CREATED)


    def put(self, obj):

        return Response({}, status=status.HTTP_202_ACCEPTED)


class WashHandsDetails(RetrieveAPIView):
    serializer_class = TeamReduceSerializer

    def get(self, request, *args, **kwargs):
        division = request.division

        return TeamReduce.objects.filter(division=division)