from django.db import models

# Create your models here.

class PatientRegister(models.Model):
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    class Meta:
        db_table = "patient_register"