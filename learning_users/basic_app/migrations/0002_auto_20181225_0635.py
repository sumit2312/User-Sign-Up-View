# Generated by Django 2.2 on 2018-12-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pic',
            new_name='profile_pics',
        ),
    ]
