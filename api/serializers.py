from rest_framework import serializers
from .models import *


# Patient Register Serializer
class PatientRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegister
        fields = ['firstname', 'lastname', 'username',
                  'email','phone_number', 'password1', 'password2']


# Patient Login Serializer
class PatientLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegister
        fields = ['username', 'password1']


# # Patient Display Serializer
# class PatientDisplaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PatientRegister
#         fields = '_all_'


# Tech Support Register Serializer
class TechRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechRegister
        fields = ['name', 'username', 'email', 'phone_number',
                  'address', 'password1', 'password2']


# Tech Support Login Serializer
class TechLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechRegister
        fields = ['username', 'password1']


# # Tech Display Serializer
# class TechtDisplaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TechRegister
#         fields = '_all_'


# Doctor Register Serializer
class DoctorRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegister
        fields = ['name', 'username', 'email', 'phone_number',
                  'hospital_address', 'password1', 'password2']


# Doctor Login Serializer
class DoctorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegister
        fields = ['username', 'password1']


# # Doctor Display Serializer
# class DoctorDisplaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DoctorRegister
#         fields = '_all_'