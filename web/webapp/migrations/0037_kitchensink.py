# Generated by Django 3.0.6 on 2020-07-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0036_snp'),
    ]

    operations = [
        migrations.CreateModel(
            name='kitchensink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('text1', models.CharField(max_length=100)),
                ('text2', models.CharField(max_length=1000)),
            ],
        ),
    ]
