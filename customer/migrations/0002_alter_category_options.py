# Generated by Django 4.2.10 on 2024-03-03 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name'], 'verbose_name_plural': 'categories'},
        ),
    ]
