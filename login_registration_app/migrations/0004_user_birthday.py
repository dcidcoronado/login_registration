# Generated by Django 3.2.4 on 2021-07-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '0003_auto_20210707_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]