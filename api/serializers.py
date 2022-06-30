from rest_framework import serializers
from .models import PatientRegister


class PatientRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegister
        fields = ['firstname','lastname','username','email','password1','password2']

class PatientLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegister
        fields = ['username','password1']