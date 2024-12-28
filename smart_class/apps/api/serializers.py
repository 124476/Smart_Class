from rest_framework import serializers
from apps.class_work.models import Work, Computer


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'user', 'name']


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['id', 'uuid', 'name', 'work', 'is_active', 'signal']
