from rest_framework import serializers
from . import models


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = "__all__"
