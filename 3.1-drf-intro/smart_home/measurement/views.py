# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import json

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    ListCreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(ListAPIView):
    def post(self, request):
        request_data = json.loads(request.body.decode())
        new_measurement = Measurement(sensor_id=Sensor.objects.get(id=int(request_data['sensor'])), temperature=request_data['temperature'])
        new_measurement.save()
        return Response({'status': 'OK'})


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        return Response({'status': 'OK'})
