# Generated by Django 4.2.4 on 2024-08-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0036_alter_gtype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuchers',
            name='oneprodact',
            field=models.BooleanField(default=False),
        ),
    ]
