# Generated by Django 5.0.1 on 2024-02-09 18:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('sub_title', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='post_image/', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='Write title', max_length=255, verbose_name='title')),
                ('author', models.CharField(help_text='Write author', max_length=30, verbose_name='author')),
                ('photo', models.ImageField(default='default', upload_to='shop/photos/', verbose_name='photo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
