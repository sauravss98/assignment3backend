# Generated by Django 4.0.5 on 2022-07-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapplication', '0009_productdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='imageURL',
            field=models.URLField(max_length=10000),
        ),
    ]
