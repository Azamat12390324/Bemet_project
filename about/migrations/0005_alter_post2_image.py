# Generated by Django 5.0.1 on 2024-02-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_remove_post2_photo_post2_image_alter_post2_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post2',
            name='image',
            field=models.ImageField(upload_to='post/image', verbose_name='image'),
        ),
    ]