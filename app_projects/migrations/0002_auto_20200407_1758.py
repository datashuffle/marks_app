# Generated by Django 3.0.4 on 2020-04-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='app_projects/images/'),
        ),
    ]
