from django.urls import path
from rest_framework_nested import routers
from .import views

router=routers.DefaultRouter()
router.register('bus_stop',views.BusStopViewSet)
router.register('bus',views.BusViewSet)
router.register('bus_time',views.BusTimeViewSet)
# router.register('bus_stop_bus_view',views.BusStopBusViewSet)


urlpatterns = router.urls
