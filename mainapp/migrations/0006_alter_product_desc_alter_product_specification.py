# Generated by Django 4.1.2 on 2022-12-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_product_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, null=True),
        ),
    ]
