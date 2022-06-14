# Generated by Django 2.2.24 on 2022-06-14 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20220613_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]
