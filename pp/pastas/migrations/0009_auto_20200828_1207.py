# Generated by Django 3.0.3 on 2020-08-28 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastas', '0008_auto_20200828_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pasta',
            old_name='clean',
            new_name='safe',
        ),
    ]
