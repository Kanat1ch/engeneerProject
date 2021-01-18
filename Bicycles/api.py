from .models import Marks, Type, Frame, Wheels, Bsles
from rest_framework import viewsets, permissions
from .serializers import MarksSerializer, TypeSerializer, FrameSerializer, WheelsSerializer, BslesSerializer


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

class FrameViewSet(viewsets.ModelViewSet):
    queryset = Frame.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FrameSerializer

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