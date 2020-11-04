# Generated by Django 3.1.2 on 2020-11-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_auto_20201103_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamWorkOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='img')),
            ],
            options={
                'verbose_name_plural': 'Team Work One',
            },
        ),
        migrations.CreateModel(
            name='TeamWorkThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='img')),
            ],
            options={
                'verbose_name_plural': 'Team Work Three',
            },
        ),
        migrations.CreateModel(
            name='TeamWorkTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='img')),
            ],
            options={
                'verbose_name_plural': 'Team Work Two',
            },
        ),
    ]
