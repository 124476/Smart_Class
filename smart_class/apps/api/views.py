__all__ = ()

from rest_framework import generics, permissions
from apps.class_work.models import Work, Computer
from apps.api.serializers import WorkSerializer, ComputerSerializer


class WorkListView(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Work.objects.all()


class WorkDetailView(generics.RetrieveAPIView):
    serializer_class = WorkSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Work.objects.all()


class ComputerListView(generics.ListAPIView):
    serializer_class = ComputerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Computer.objects.all()


class ComputerDetailView(generics.RetrieveAPIView):
    serializer_class = ComputerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Computer.objects.all()
