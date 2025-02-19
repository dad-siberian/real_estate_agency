# Generated by Django 3.2 on 2022-10-18 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0013_auto_20221014_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complained_flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_complaints', to='property.flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
