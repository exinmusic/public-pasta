# Generated by Django 3.0.3 on 2020-02-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastas', '0003_auto_20200217_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='name',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='text',
            field=models.TextField(max_length=3500),
        ),
    ]
