# Generated by Django 5.0.1 on 2024-02-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_post_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]