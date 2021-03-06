# Generated by Django 3.0.6 on 2020-06-08 15:50

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
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(default='null', max_length=200)),
                ('message', models.CharField(default='null', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(default='null', max_length=200)),
                ('message', models.CharField(default='null', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('mobilenumber', models.IntegerField(default=0, max_length=10)),
                ('password1', models.CharField(default='null', max_length=20)),
                ('password2', models.CharField(default='null', max_length=20)),
                ('address', models.CharField(default='null', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('mobilenumber', models.IntegerField(default=0, max_length=10)),
                ('address', models.CharField(default='null', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='supplementsOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onwhey', models.IntegerField(default=0)),
                ('pro', models.IntegerField(default=0)),
                ('mbgold', models.IntegerField(default=0)),
                ('mpwhey', models.IntegerField(default=0)),
                ('rcking', models.IntegerField(default=0)),
                ('mtmass', models.IntegerField(default=0)),
                ('syntha', models.IntegerField(default=0)),
                ('onmass', models.IntegerField(default=0)),
                ('onbcaa', models.IntegerField(default=0)),
                ('mbmulti', models.IntegerField(default=0)),
                ('mpcreatine', models.IntegerField(default=0)),
                ('glutamine', models.IntegerField(default=0)),
                ('asitis', models.IntegerField(default=0)),
                ('onshaker', models.IntegerField(default=0)),
                ('gymeq', models.IntegerField(default=0)),
                ('gymbag', models.IntegerField(default=0)),
                ('totalSum', models.BigIntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
