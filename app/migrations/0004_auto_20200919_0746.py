# Generated by Django 2.2 on 2020-09-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_newsdetails_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdetails',
            name='author',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Author Name'),
        ),
    ]
