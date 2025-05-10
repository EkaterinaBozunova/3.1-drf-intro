from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.sensor.name} at {self.timestamp}: {self.temperature}"