from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from django.core.exceptions import PermissionDenied
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

    def destroy(self, request, *args, **kwargs):
        bus = self.get_object()
        if self.request.user.is_staff:
            bus.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied("You are not allowed to delete this object.")

class BusTimeViewSet(ModelViewSet):
    queryset=BusTime.objects.all()
    serializer_class=BusTimeSerializer


    def get_permissions(self):
        # permission_classes = []
        # if self.request.method in ['create','update','destroy','retrieve']:
        #     print(self.request.user)
        #     permission_classes=[IsAuthenticated]
        if self.request.method =='GET':
            print("xcxv")
            # permission_classes= [AllowAny]
            return [AllowAny()]
        else:
            print("asfsf")
            # permission_classes = [IsAuthenticated]
            return [IsAuthenticated()]
    
    #     # elif self.request == 'create':
    #     #     permission_classes = [IsAdminUser]
    #     # elif self.request == 'retrieve':
    #     #     permission_classes = [IsAdminUser]
    #     # elif self.request == 'update':
    #     #     permission_classes = [IsAdminUser]
    #     # elif self.request == 'destroy':
    #     #     permission_classes =[IsAdminUser]
        # return [permission() for permission in permission_classes ]

    # def get_permissions(self):
    #     permission_classes = []
    #     print("Request:", self.request)
    #     if self.request =='list':
    #         permission_classes= [AllowAny]
    #     elif self.request == 'create':
    #         permission_classes = [IsAdminUser]
    #     elif self.request == 'retrieve':
    #         permission_classes = [AllowAny]
    #     elif self.request == 'update':
    #         permission_classes = [IsAdminUser]
    #     elif self.request == 'destroy':
    #         permission_classes =[IsAdminUser]
    #     print("Permission Classes:", permission_classes)
    #     return [permission() for permission in permission_classes ]

    # def has_permissions(self,request):
    #     permission_classes = []
    #     if self.request.method =='GET':
    #         permission_classes=[AllowAny]
    #     else:
    #         permission_classes=IsAuthenticated
    #     return [permission() for permission in permission_classes ]
        

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
        
    # def create(self, request, *args, **kwargs):
    #     serializer = BusTimeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # print (self.request.user.role
    #         #     )
    #         if self.request.user.is_staff:
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             raise PermissionDenied("You are not allowed to create this object.")
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    # def destroy(self, request, *args, **kwargs):
    #     bus_time = self.get_object()
    #     if self.request.user.is_staff:
    #         bus_time.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         raise PermissionDenied("You are not allowed to delete this object.")

    # def update(self, request, *args, **kwargs):
    #     bus_time = self.get_object()
    #     serializer = BusTimeSerializer(bus_time, data=request.data)
    #     if serializer.is_valid():
    #         if self.request.user.is_staff:
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             raise PermissionDenied("You are not allowed to update this object.")
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    



