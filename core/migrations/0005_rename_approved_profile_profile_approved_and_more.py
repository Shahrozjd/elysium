# Generated by Django 4.0.4 on 2022-07-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_country_profile_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='approved',
            new_name='profile_approved',
        ),
        migrations.AddField(
            model_name='profile',
            name='membership_expires_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
