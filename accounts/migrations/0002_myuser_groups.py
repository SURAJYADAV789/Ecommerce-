# Generated by Django 3.2.9 on 2022-02-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
