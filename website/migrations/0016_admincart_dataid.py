# Generated by Django 4.1.7 on 2023-05-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_admincart'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincart',
            name='dataid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
