# Generated by Django 3.0.8 on 2020-07-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20200704_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beetname',
            name='id',
        ),
        migrations.RemoveField(
            model_name='beetsize',
            name='id',
        ),
        migrations.RemoveField(
            model_name='godown',
            name='id',
        ),
        migrations.RemoveField(
            model_name='othersname',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plysize',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plythickness',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='beetname',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='beetsize',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='godown',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='othersname',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plysize',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plythickness',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
