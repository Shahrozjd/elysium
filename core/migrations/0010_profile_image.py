# Generated by Django 4.0.4 on 2022-07-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_source_profile_purpose_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
