# Generated by Django 5.0.6 on 2024-05-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_img_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=44)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
    ]