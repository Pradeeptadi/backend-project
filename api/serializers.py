from rest_framework import serializers
from .models import WheelSpecification
from datetime import date

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

    def validate_formNumber(self, value):
        if not value.startswith('WHEEL-'):
            raise serializers.ValidationError("formNumber must start with 'WHEEL-'")
        return value

    def validate_submittedDate(self, value):
        if value > date.today():
            raise serializers.ValidationError("submittedDate cannot be in the future.")
        return value
