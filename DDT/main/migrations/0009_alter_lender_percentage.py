# Generated by Django 3.2.10 on 2021-12-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_lender_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lender',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]
