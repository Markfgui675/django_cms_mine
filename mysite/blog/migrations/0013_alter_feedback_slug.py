# Generated by Django 5.0.3 on 2024-04-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_blogpage_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='slug',
            field=models.CharField(blank=True, max_length=250, verbose_name='Slug'),
        ),
    ]