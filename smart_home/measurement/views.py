from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer

# Для работы с списком и созданием датчиков
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Для получения, редактирования и удаления конкретного датчика
class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'id'

# Для создания новых измерений
class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer