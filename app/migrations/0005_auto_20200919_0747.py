# Generated by Django 2.2 on 2020-09-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200919_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdetails',
            name='author',
            field=models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Author Name'),
        ),
    ]
