# Generated by Django 3.1.4 on 2021-03-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./static/habit-images'),
        ),
    ]