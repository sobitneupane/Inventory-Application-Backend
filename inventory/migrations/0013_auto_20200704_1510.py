# Generated by Django 3.0.8 on 2020-07-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20200704_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plywood',
            name='godown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Godown'),
        ),
        migrations.AlterField(
            model_name='plywood',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlySize'),
        ),
        migrations.AlterField(
            model_name='plywood',
            name='thickness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlyThickness'),
        ),
        migrations.AlterField(
            model_name='waterproof',
            name='godown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Godown'),
        ),
        migrations.AlterField(
            model_name='waterproof',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlySize'),
        ),
        migrations.AlterField(
            model_name='waterproof',
            name='thickness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlyThickness'),
        ),
    ]
