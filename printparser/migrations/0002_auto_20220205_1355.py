# Generated by Django 3.0 on 2022-02-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prints',
            name='created_at',
            field=models.CharField(max_length=200, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='prints',
            name='updated_at',
            field=models.CharField(max_length=200, verbose_name='Обновлено в'),
        ),
    ]
