# Generated by Django 3.2 on 2022-10-18 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20221018_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owned_flat',
            new_name='flats',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
