# Generated by Django 5.0.3 on 2024-04-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogpage_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='author',
        ),
    ]
