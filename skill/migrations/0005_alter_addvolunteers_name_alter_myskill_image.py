# Generated by Django 4.0.3 on 2022-05-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0004_addvolunteers_alter_userregister_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvolunteers',
            name='Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='myskill',
            name='image',
            field=models.ImageField(upload_to='skillimage'),
        ),
    ]
