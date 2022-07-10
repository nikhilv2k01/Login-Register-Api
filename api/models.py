from django.db import models
# Create your models here.


# Patient Register
class PatientRegister(models.Model):
    patient_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    class Meta:
        db_table = "patient_register"


# Tech Support Register
class TechRegister(models.Model):
    tech_id = models.AutoField(primary_key=True)
    patient_fk = models.ForeignKey(PatientRegister,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.BigIntegerField()
    address = models.TextField(max_length=150)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    class Meta:
        db_table = "tech_register"


# Doctor Register
class DoctorRegister(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    patient_fk = models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.BigIntegerField()
    hospital_address = models.TextField(max_length=150)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    class Meta:
        db_table = "doctor_register"
