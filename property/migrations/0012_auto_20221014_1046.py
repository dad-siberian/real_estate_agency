# Generated by Django 3.2 on 2022-10-14 07:46

from django.db import migrations


def link_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    if owners.exists():
        for owner in owners.iterator():
            flats = Flat.objects.filter(owner=owner.owner)
            owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20221014_1042'),
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners),
    ]
