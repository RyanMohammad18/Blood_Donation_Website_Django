# Generated by Django 4.0.3 on 2022-05-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0007_remove_myskill_email_myskill_descc'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyVolunteerSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='skillimage')),
                ('Name', models.CharField(max_length=50)),
                ('BloodGroup', models.TextField(blank=True, max_length=500)),
                ('Address', models.TextField(blank=True, max_length=500)),
                ('email', models.EmailField(blank=True, max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]