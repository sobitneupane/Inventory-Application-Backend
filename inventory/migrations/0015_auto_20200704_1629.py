# Generated by Django 3.0.8 on 2020-07-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20200704_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plywood',
            name='godown',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='plywood',
            name='size',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='plywood',
            name='thickness',
            field=models.CharField(max_length=20),
        ),
    ]
