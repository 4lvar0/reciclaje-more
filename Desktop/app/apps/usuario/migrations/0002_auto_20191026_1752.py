# Generated by Django 2.2.6 on 2019-10-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='username',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
