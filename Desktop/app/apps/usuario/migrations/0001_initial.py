# Generated by Django 2.2.6 on 2019-11-07 19:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(default=0, max_length=30)),
                ('apellido', models.CharField(default=0, max_length=30)),
                ('correoElectronico', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=12, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='noticias',
            fields=[
                ('codigoNoticia', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(default='Missing', max_length=70)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('descripcion', models.CharField(max_length=500)),
                ('Imagen', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='proveedorRecompensa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('Logo', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='recompensa',
            fields=[
                ('idrecompensa', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('expiracion', models.DateField(null=True)),
                ('activo', models.BooleanField(default=False)),
                ('costo', models.IntegerField(default=0)),
                ('idproveedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.proveedorRecompensa')),
            ],
        ),
        migrations.CreateModel(
            name='Reciclaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadReciclada', models.FloatField(default=0)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('tipoMaterial', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(default=0)),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
