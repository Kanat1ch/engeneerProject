from rest_framework import serializers
from .models import Transmissions, Marks, Ranks, Cars


class TransmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = '__all__'

class RanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = '__all__'

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = '__all__'



