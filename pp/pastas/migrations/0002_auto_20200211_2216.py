# Generated by Django 3.0.3 on 2020-02-11 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='category',
            field=models.CharField(blank=True, choices=[('wholesome', 'wholesome'), ('sermon', 'sermon'), ('intelligent', 'intelligent'), ('funny', 'funny'), ('sad', 'sad'), ('politics', 'politics'), ('flagged', 'flagged')], default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='text',
            field=models.TextField(max_length=2000),
        ),
    ]
