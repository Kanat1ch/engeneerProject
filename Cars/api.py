from .models import Transmissions, Marks, Ranks, Cars
from rest_framework import viewsets, permissions
from .serializers import TransmissionsSerializer, MarksSerializer, RanksSerializer, CarsSerializer


class TransmissionsViewSet(viewsets.ModelViewSet):
    queryset = Transmissions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TransmissionsSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarksSerializer

class RanksViewSet(viewsets.ModelViewSet):
    queryset = Transmissions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RanksSerializer

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarsSerializer