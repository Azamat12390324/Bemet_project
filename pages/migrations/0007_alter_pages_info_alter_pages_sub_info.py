# Generated by Django 5.0.1 on 2024-02-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_pages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='info',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pages',
            name='sub_info',
            field=models.CharField(max_length=255),
        ),
    ]
