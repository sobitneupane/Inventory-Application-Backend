# Generated by Django 3.0.8 on 2020-07-04 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0016_auto_20200704_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('godown', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BeetName',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='beet/')),
            ],
        ),
        migrations.CreateModel(
            name='BeetSize',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Godown',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('godown', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='others/')),
            ],
        ),
        migrations.CreateModel(
            name='OthersName',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='others/')),
            ],
        ),
        migrations.CreateModel(
            name='PlySize',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlyThickness',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='ply/')),
            ],
            options={
                'verbose_name': 'Ply Thickness',
                'verbose_name_plural': 'Ply Thickness',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WaterProof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('godown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Godown')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlySize')),
                ('thickness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlyThickness')),
            ],
        ),
        migrations.CreateModel(
            name='Plywood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('godown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Godown')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlySize')),
                ('thickness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PlyThickness')),
            ],
        ),
    ]
