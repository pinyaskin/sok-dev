# Generated by Django 3.2.6 on 2021-09-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_table', '0009_history_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('callerid', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('post_number', models.IntegerField(blank=True, null=True)),
                ('name_object', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('lastcall', models.TextField(blank=True, null=True)),
                ('commentary', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'posts',
                'managed': False,
            },
        ),
    ]
