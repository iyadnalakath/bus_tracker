from rest_framework import serializers
from .models import *
from main.functions import get_auto_id

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusStop
        fields=[
            'id',
            'bus_stop_name',
            'location'
        ]

        extra_kwargs={
            'auto_id':{'read_only':True}
        }

    def create(self, validated_data):
        bus_stop=BusStop.objects.create(
            **validated_data,
            auto_id=get_auto_id(BusStop),
            # creator = self.context['request'].user
        )
        return  bus_stop


class BusSerializer(serializers.ModelSerializer):
    # bus_stop_name=serializers.CharField(source='bus_stop.bus_stop_name',read_only=True)
    class Meta:
        model=Bus
        fields=[
            'id',
            'bus_name',
            'route',
           
        ]


        extra_kwargs={
            'auto_id':{'read_only':True}
        }

    def create(self, validated_data):
        bus=Bus.objects.create(
            **validated_data,
            auto_id=get_auto_id(Bus),
            # creator = self.context['request'].user
        )
        return  bus



class BusTimeSerializer(serializers.ModelSerializer):
    bus_stop_name=serializers.CharField(source='bus_stop.bus_stop_name',read_only=True)
    bus_name=serializers.CharField(source='bus.bus_name',read_only=True)

    class Meta:
        model=BusTime
        fields=[
            'id',
            'bus_stop',
            'bus_stop_name',
            'bus',
            'bus_name',
            'time'
        ]

        extra_kwargs={
            'auto_id':{'read_only':True}
        }

    def create(self, validated_data):
        bus_time=BusTime.objects.create(
            **validated_data,
            auto_id=get_auto_id(BusTime),
            # creator = self.context['request'].user
        )
        return  bus_time


# class BusStopBusViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Bus
#         fields=[
#             'id',
#             'bus_name'
#             'bus_stop_name',
#             'route'
#         ]
#         extra_kwargs={
#             'auto_id':{'read_only':True}
#         }

#     def create(self, validated_data):
#         bus=Bus.objects.create(
#             **validated_data,
#             auto_id=get_auto_id(Bus),
#             # creator = self.context['request'].user
#         )
#         return  bus

