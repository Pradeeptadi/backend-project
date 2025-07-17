from django import forms
from .models import WheelSpecification

class WheelSpecificationForm(forms.ModelForm):
    class Meta:
        model = WheelSpecification
        fields = '__all__'
