# Generated by Django 4.1.1 on 2023-02-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
