# Generated by Django 3.2.7 on 2021-11-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
