# Generated by Django 3.2.9 on 2021-11-14 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theeyeservice', '0004_auto_20211113_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='payload',
        ),
        migrations.RemoveField(
            model_name='payload',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='data',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='theeyeservice.payload'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payload',
            name='form',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='theeyeservice.form'),
        ),
        migrations.AlterField(
            model_name='form',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='payload',
            name='element',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
