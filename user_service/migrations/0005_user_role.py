# Generated by Django 2.1.1 on 2018-09-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0004_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='user_service.Role'),
        ),
    ]