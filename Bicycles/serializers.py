from rest_framework import serializers
from .models import Marks, Type, Frame, Wheels, Bsles


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = '__all__'

class WheelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheels
        fields = '__all__'

class BslesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bsles
        fields = '__all__'
