# Generated by Django 3.0.3 on 2020-02-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200216_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdatetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatedatetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]