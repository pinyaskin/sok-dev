# Generated by Django 3.2.6 on 2021-09-08 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_table', '0002_auto_20210908_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='callerid',
            new_name='caller',
        ),
    ]
