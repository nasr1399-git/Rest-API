# Generated by Django 3.0.3 on 2020-02-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='owener',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatedatetime',
            field=models.DateTimeField(),
        ),
    ]