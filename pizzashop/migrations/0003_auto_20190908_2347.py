# Generated by Django 2.2.5 on 2019-09-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0002_auto_20190908_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzashop',
            name='logo',
            field=models.ImageField(upload_to='pizzashop_logo/', verbose_name='Лого  '),
        ),
    ]
