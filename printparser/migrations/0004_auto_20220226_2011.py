# Generated by Django 3.0 on 2022-02-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printparser', '0003_auto_20220209_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prints',
            name='blueprint',
            field=models.TextField(blank=True, null=True, verbose_name='Строка чертежа'),
        ),
        migrations.AlterField(
            model_name='prints',
            name='details',
            field=models.TextField(blank=True, null=True, verbose_name='Подробности'),
        ),
    ]
