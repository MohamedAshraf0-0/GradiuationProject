# Generated by Django 4.1.4 on 2022-12-14 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=60)),
                ('ProfileImage', models.ImageField(upload_to='Photos/DoctorsProfilesPhotos/%y/%m/%d')),
                ('DepartmentID', models.CharField(choices=[('Neurologists', 'Neurologists'), ('Chest', 'Chest')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SessionStart', models.DateTimeField()),
                ('SessionEnd', models.DateTimeField()),
                ('DoctorID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.TextField(max_length=25)),
                ('Image', models.ImageField(upload_to='Photos/PostsImages/%y/%m/%d')),
                ('DoctorID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Doctors.doctor')),
            ],
        ),
    ]
