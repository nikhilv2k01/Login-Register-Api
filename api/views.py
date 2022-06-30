from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import PatientRegister
from .serializers import PatientRegSerializer, PatientLoginSerializer
from django.db.models import Q
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def patient_register(request):

    patient_data = JSONParser().parse(request)
    patient_serializer = PatientRegSerializer(data=patient_data)

    queryset = PatientRegister.objects.filter(
        Q(username=patient_data['username']) | Q(email=patient_data['email']))

    password1 = patient_data['password1']
    password2 = patient_data['password2']

    if patient_serializer.is_valid():
        if not queryset:
            if password1 == password2:
                patient_serializer.save()
                return JsonResponse({'message': 'Patient registered successfully'})
            else:
                return JsonResponse({'message': 'Password does not match'})
        else:
            return JsonResponse({'message': 'Email or Username already exist'})

    return JsonResponse(patient_serializer.errors)


@api_view(['POST'])
def patient_login(request):

    patient_data = JSONParser().parse(request)
    patient_serializer = PatientLoginSerializer(data=patient_data)

    user_name = patient_data['username']
    password = patient_data['password1']

    if '@' in user_name:
        user_exist = PatientRegister.objects.filter(
            email=user_name, password1=password).exists()

    else:
        user_exist = PatientRegister.objects.filter(
            username=user_name, password1=password).exists()

    if patient_serializer.is_valid():
        if user_exist:
            return JsonResponse({'message': 'Success'})
        else:
            return JsonResponse({'message': 'Please enter a vaild details'})
    return JsonResponse(patient_serializer.errors)
