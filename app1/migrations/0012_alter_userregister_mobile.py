# Generated by Django 5.0.6 on 2024-06-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_userregister_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
    ]
