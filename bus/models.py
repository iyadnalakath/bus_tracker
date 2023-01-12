from django.db import models
from main.models import BaseModel

# Create your models here.

class BusStop(BaseModel):
    bus_stop_name=models.CharField(max_length=255,default="")
    location=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.bus_stop_name


# class Bus(BaseModel):
#     bus_name=models.CharField(max_length=255,null=True,blank=True)
#     route=models.CharField(max_length=255,null=True,blank=True)
#     bus_stop=models.ForeignKey(BusStop,on_delete=models.CASCADE)
#     time=models.CharField(max_length=255,null=True,blank=True)





class Bus(BaseModel):
    bus_name=models.CharField(max_length=255,null=True,blank=True)
    route=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) -> str:
        return self.bus_name

class BusTime(BaseModel):
    bus_stop=models.ForeignKey(BusStop,on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    # time=models.CharField(max_length=255,null=True,blank=True)
    time=models.TimeField(null=True,blank=True)





