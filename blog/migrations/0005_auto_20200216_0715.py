# Generated by Django 3.0.3 on 2020-02-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200216_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdatetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatedatetime',
            field=models.DateTimeField(),
        ),
    ]
