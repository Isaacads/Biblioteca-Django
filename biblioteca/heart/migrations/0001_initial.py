# Generated by Django 3.0.8 on 2020-07-06 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Ed', models.CharField(max_length=100)),
                ('Nome', models.CharField(max_length=50)),
                ('Edereco', models.CharField(max_length=100)),
                ('Telefone', models.CharField(max_length=14)),
                ('Site', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Li', models.CharField(max_length=100)),
                ('Nome', models.CharField(max_length=100)),
                ('Autor', models.CharField(max_length=100)),
                ('Observacao', models.CharField(max_length=100)),
                ('Imag', models.ImageField(upload_to='capas')),
                ('Editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heart.Editora')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(verbose_name=True)),
                ('senha', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Reservar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Devolver', models.DateTimeField()),
                ('Nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Nome_liv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heart.Livro')),
            ],
        ),
    ]