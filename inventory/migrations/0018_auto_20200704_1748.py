# Generated by Django 3.0.8 on 2020-07-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_beet_beetname_beetsize_godown_others_othersname_plysize_plythickness_plywood_product_waterproof'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plysize',
            options={'verbose_name': 'Ply Size', 'verbose_name_plural': 'Ply Size'},
        ),
        migrations.AlterField(
            model_name='plywood',
            name='size',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='waterproof',
            name='size',
            field=models.CharField(max_length=20),
        ),
    ]
