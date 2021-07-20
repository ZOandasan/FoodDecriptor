# Generated by Django 3.2.3 on 2021-07-20 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_side'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='side',
            field=models.ManyToManyField(to='main_app.Side'),
        ),
        migrations.AlterField(
            model_name='side',
            name='taste',
            field=models.CharField(choices=[('SW', 'Sweet'), ('SO', 'Sour'), ('NA', 'Salty'), ('BI', 'Bitter'), ('SA', 'Savory')], default='SW', max_length=2, verbose_name='taste'),
        ),
    ]