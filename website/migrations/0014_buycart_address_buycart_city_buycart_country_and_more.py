# Generated by Django 4.1.7 on 2023-05-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_delete_carbuy_buycart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buycart',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='buycart',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='buycart',
            name='country',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='buycart',
            name='firstname',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='buycart',
            name='lastname',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='buycart',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
