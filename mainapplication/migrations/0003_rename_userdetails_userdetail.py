# Generated by Django 4.0.5 on 2022-07-25 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapplication', '0002_userdetails_delete_employeedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]
