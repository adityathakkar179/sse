# Generated by Django 3.0.6 on 2020-05-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ultratech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('text1', models.CharField(default='sample', max_length=100)),
                ('text2', models.CharField(default='Sample', max_length=1000)),
            ],
        ),
    ]
