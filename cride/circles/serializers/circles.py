

# DRF
from rest_framework import serializers

# Models
from cride.circles.models.circles import Circle

class CircleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Circle
        fields = ['name', 'about', 'rides_offered', 'is_public']
