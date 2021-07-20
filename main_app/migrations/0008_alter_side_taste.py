# Generated by Django 3.2.3 on 2021-07-20 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_side_food_sides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='side',
            name='taste',
            field=models.CharField(choices=[('SWEET', 'Sweet'), ('SOUR', 'Sour'), ('SALTY', 'Salty'), ('BITTER', 'Bitter'), ('SAVORY', 'Savory')], default='SWEET', max_length=7, verbose_name='taste'),
        ),
    ]