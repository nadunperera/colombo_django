# Generated by Django 2.1.1 on 2018-09-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0004_auto_20180913_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(related_name='users', to='user_service.Role'),
        ),
    ]
