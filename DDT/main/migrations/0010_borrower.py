# Generated by Django 3.2.10 on 2021-12-29 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_alter_lender_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('conditions', models.TextField()),
                ('Lender_approval', models.BooleanField(default=False)),
                ('Borrower_approval', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]