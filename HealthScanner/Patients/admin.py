from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.BrainMRI)
admin.site.register(models.ChestMRI)
admin.site.register(models.Patient)
