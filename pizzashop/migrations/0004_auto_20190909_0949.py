# Generated by Django 2.2.5 on 2019-09-09 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0003_auto_20190908_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzashop',
            name='logo',
            field=models.ImageField(upload_to='pizzashop_logo/', verbose_name='Логотип:'),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pizza_imsges/')),
                ('price', models.IntegerField(default=0)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashop.PizzaShop')),
            ],
        ),
    ]
