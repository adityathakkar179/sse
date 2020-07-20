# Generated by Django 3.0.6 on 2020-07-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0040_ecws'),
    ]

    operations = [
        migrations.CreateModel(
            name='electronicflushing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('text1', models.CharField(max_length=100)),
                ('text2', models.CharField(max_length=1000)),
            ],
        ),
    ]
