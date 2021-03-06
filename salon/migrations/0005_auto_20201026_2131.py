# Generated by Django 3.1 on 2020-10-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_auto_20201026_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Massage',
            },
        ),
        migrations.AlterModelOptions(
            name='eyebrows',
            options={'verbose_name_plural': 'Eyebrows & Eyelashes'},
        ),
        migrations.AlterModelOptions(
            name='haircolouring',
            options={'verbose_name_plural': 'Colouring & Highlights'},
        ),
        migrations.AlterModelOptions(
            name='haircutting',
            options={'verbose_name_plural': 'Haircuts & Hairdressing'},
        ),
        migrations.AlterModelOptions(
            name='ladieswaxing',
            options={'verbose_name_plural': "Ladie's Waxing"},
        ),
        migrations.AlterModelOptions(
            name='menswaxing',
            options={'verbose_name_plural': "Men's Waxing"},
        ),
        migrations.AlterModelOptions(
            name='waxpackage',
            options={'verbose_name_plural': 'Ladies Waxing - Packages'},
        ),
    ]
