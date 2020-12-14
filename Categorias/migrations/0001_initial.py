# Generated by Django 2.2.14 on 2020-12-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=700)),
                ('fecha_de_creacion', models.DateField()),
            ],
        ),
    ]