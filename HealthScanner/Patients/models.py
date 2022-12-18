from django.db import models
import time
# Create your models here.
class Patient(models.Model):
    FirstName    = models.CharField(max_length=25)
    LastName     = models.CharField(max_length=25)
    Email        = models.CharField(max_length=50, unique=True)
    Password     = models.CharField(max_length=60)
    Birthdate    = models.DateField(null=False)
    ImageProfile = models.ImageField(upload_to='Photos/PatientsProfilesPhoto/%y/%m/%d')

class ChestMRI(models.Model):
    PredictValue = models.CharField(max_length=60)
    Image        = models.ImageField(upload_to='Photos/ChestMRI/%y/%m/%d')
    PatientID    = models.ForeignKey(Patient, on_delete=models.PROTECT)


class BrainMRI(models.Model):
    PredictValue = models.CharField(max_length=60)
    Image        = models.ImageField(upload_to='Photos/BrainMRI/%y/%m/%d')
    PatientID    = models.ForeignKey(Patient, on_delete=models.PROTECT)
