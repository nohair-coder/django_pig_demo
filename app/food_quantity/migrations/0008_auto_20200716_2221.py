# Generated by Django 3.0.8 on 2020-07-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_quantity', '0007_auto_20200715_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodquantity',
            name='pigid',
            field=models.CharField(max_length=16, verbose_name='身份码'),
        ),
        migrations.AlterField(
            model_name='foodquantity',
            name='settime',
            field=models.DateField(default='2020-07-16', verbose_name='设置日期'),
        ),
    ]
