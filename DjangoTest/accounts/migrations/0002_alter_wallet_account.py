# Generated by Django 4.1.4 on 2023-01-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.account'),
        ),
    ]