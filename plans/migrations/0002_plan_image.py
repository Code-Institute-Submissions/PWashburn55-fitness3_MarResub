# Generated by Django 3.1.4 on 2021-01-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]