# Generated by Django 3.0.8 on 2020-07-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pig_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigbase',
            name='addpigtime',
            field=models.DateField(default='2020-07-13', verbose_name='入栏日期'),
        ),
    ]
