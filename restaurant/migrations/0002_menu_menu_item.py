# Generated by Django 4.1.7 on 2024-02-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_item',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
