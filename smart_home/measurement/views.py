from rest_framework import generics
from .models import ViewModel
from .serializers import ViewSerializer

class ViewListCreate(generics.ListCreateAPIView):
    queryset = ViewModel.objects.all()
    serializer_class = ViewSerializer

class ViewRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = ViewModel.objects.all()
    serializer_class = ViewSerializer