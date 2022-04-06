# Generated by Django 3.2.9 on 2022-02-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('contact', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]