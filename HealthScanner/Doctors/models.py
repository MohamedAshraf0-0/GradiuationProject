from django.db import models

# Create your models here.


class Doctor(models.Model):
    DepartmentsChoise = [
        ('Neurologists', 'Neurologists'),
        ('Chest', 'Chest')
    ]
    FirstName    = models.CharField(max_length=25)
    LastName     = models.CharField(max_length=25)
    Email        = models.CharField(max_length=50, unique=True)
    Password     = models.CharField(max_length=60)
    ProfileImage = models.ImageField(upload_to='Photos/DoctorsProfilesPhotos/%y/%m/%d')
    DepartmentID = models.CharField(max_length=25, choices=DepartmentsChoise)

class Post(models.Model):
    Content  = models.TextField(max_length=25)
    Image    = models.ImageField(upload_to='Photos/PostsImages/%y/%m/%d')
    DoctorID = models.ForeignKey(Doctor, on_delete=models.PROTECT)

class Session(models.Model):
    SessionStart = models.DateTimeField()
    SessionEnd   = models.DateTimeField()
    DoctorID     = models.ForeignKey(Doctor, on_delete=models.PROTECT)