from rest_framework import serializers
from fibonacci.models import fibResult


class fibResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = fibResult
        fields = ("nthFib", "time", "number")
