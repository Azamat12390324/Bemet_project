# Generated by Django 5.0.1 on 2024-02-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_remove_service_sub_title_service_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='number',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
