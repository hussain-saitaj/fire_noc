# Generated by Django 3.2.2 on 2022-01-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firenoc_app', '0002_alter_application_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='form',
            field=models.FileField(upload_to='applications'),
        ),
    ]
