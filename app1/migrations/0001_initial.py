# Generated by Django 3.2.9 on 2022-02-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_price', models.FloatField()),
                ('p_desc', models.TextField()),
                ('p_image', models.ImageField(default='NO_image', upload_to='product_img/')),
            ],
        ),
    ]
