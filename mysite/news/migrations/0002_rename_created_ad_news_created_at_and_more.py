# Generated by Django 4.1.1 on 2023-02-01 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]