# Generated by Django 5.2.3 on 2025-06-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fill_your_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('details', models.TextField()),
                ('price', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='products')),
            ],
        ),
    ]
