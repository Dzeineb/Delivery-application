# Generated by Django 5.1.1 on 2024-09-25 21:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colis', '0002_rename_request_colis'),
    ]

    operations = [
        migrations.AddField(
            model_name='colis',
            name='region',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colis',
            name='adr_destinataire',
            field=models.CharField(max_length=30),
        ),
    ]
