# Generated by Django 5.0.1 on 2024-02-19 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_pages_info_alter_pages_sub_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pages',
            old_name='info',
            new_name='sub_title',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='sub_info',
            new_name='title',
        ),
    ]
