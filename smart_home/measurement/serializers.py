from rest_framework import serializers

from rest_framework import serializers
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

    def get_measurements(self, obj):
        measurements = obj.measurements.all()
        return [{'temperature': m.temperature, 'timestamp': m.timestamp} for m in measurements]

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']