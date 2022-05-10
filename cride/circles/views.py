

# Django
from django.http import HttpResponse

# DRF
from rest_framework import generics, viewsets

# Serializer
from cride.circles.serializers.circles import CircleModelSerializer

# Model
from cride.circles.models.circles import Circle


class CircleViewSet(generics.ListAPIView, viewsets.GenericViewSet):
    queryset = Circle.objects.filter(is_public=True)
    serializer_class = CircleModelSerializer
    model = Circle
