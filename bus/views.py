from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from .models import *
from .serializer import *
from django.db.models import Q

# Create your views here.
class BusStopViewSet(ModelViewSet):
    queryset=BusStop.objects.all()
    serializer_class=BusStopSerializer
    permission_classes= [IsAuthenticated]



class BusViewSet(ModelViewSet):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer
    permission_classes=[IsAuthenticated]

class BusTimeViewSet(ModelViewSet):
    queryset=BusTime.objects.all()
    serializer_class=BusTimeSerializer

    def get_permissions(self):
        if self.request == 'list':
            permission_classes= [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes ]

    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset().order_by('auto_id')
        if request.GET.get('bus_stop') and request.GET.get('fromtime'):
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            bus_stop=self.request.GET.get('bus_stop')
            fromtime=self.request.GET.get('fromtime')
            totime=self.request.GET.get('totime')
            # queryset=queryset.filter(Q(bus_stop=bus_stop),Q(time__gte=fromtime),Q(time__lte=totime)).order_by('auto_id')
            queryset=queryset.filter(bus_stop=bus_stop,time__gte=fromtime,time__lte=totime).order_by('auto_id')
            serializer=BusTimeSerializer(queryset,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            queryset=queryset
            serializer=BusTimeSerializer(queryset,many=True)
            # return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        



