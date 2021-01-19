from .models import Marks, Type, Wheels, Bsles
from rest_framework import viewsets, permissions
from .serializers import MarksSerializer, TypeSerializer, WheelsSerializer, BslesSerializer


class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarksSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TypeSerializer

class WheelsViewSet(viewsets.ModelViewSet):
    queryset = Wheels.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WheelsSerializer

class BslesViewSet(viewsets.ModelViewSet):
    queryset = Bsles.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BslesSerializer