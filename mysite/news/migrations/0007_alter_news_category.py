# Generated by Django 4.1.1 on 2023-02-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
    ]
