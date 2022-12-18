from django.db import models
from Doctors.models import Post
# Create your models here.

class Like(models.Model):
    PostID = models.ForeignKey(Post, on_delete=models.PROTECT)
    DoctorEmail = models.CharField(max_length=60)
    PatientEmail = models.CharField(max_length=60)

class Comment(models.Model):
    PostID       = models.ForeignKey(Post, on_delete=models.PROTECT)
    DoctorEmail  = models.CharField(max_length=60)
    PatientEmail = models.CharField(max_length=60)
    Content      = models.TextField(null=True, blank=True, default='Hi :)')
