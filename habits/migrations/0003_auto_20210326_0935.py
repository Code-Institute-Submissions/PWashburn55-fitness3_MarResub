# Generated by Django 3.1.4 on 2021-03-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_auto_20210326_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./habits/static/habit-images'),
        ),
    ]
