# Generated by Django 2.2.14 on 2020-12-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
    ]
