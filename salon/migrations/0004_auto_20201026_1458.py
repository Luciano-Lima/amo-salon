# Generated by Django 3.1 on 2020-10-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0003_eyebrows_ladyswaxing_menswaxing_nonpurchasable_waxpackage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LadysWaxing',
            new_name='LadiesWaxing',
        ),
        migrations.AlterModelOptions(
            name='ladieswaxing',
            options={'verbose_name': "Ladie's Waxing"},
        ),
    ]
