# Generated by Django 5.0.1 on 2024-02-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=50)),
                ('general', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('doctor_name', models.CharField(max_length=20)),
            ],
        ),
    ]
