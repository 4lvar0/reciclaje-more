# Generated by Django 2.2.3 on 2019-10-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20191024_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='Imagen',
            field=models.CharField(blank=True, max_length=2083),
        ),
        migrations.AlterField(
            model_name='proveedorrecompensa',
            name='Logo',
            field=models.CharField(blank=True, max_length=2083),
        ),
    ]