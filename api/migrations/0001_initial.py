# Generated by Django 4.0.5 on 2022-07-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorRegister',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('hospital_address', models.TextField(max_length=150)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'doctor_register',
            },
        ),
        migrations.CreateModel(
            name='PatientRegister',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'patient_register',
            },
        ),
        migrations.CreateModel(
            name='TechRegister',
            fields=[
                ('tech_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=150)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tech_register',
            },
        ),
    ]
