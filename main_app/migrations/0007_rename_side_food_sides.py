# Generated by Django 3.2.3 on 2021-07-20 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210720_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='side',
            new_name='sides',
        ),
    ]
