# Generated by Django 4.1.7 on 2023-05-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_cartmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='buycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productnm', models.CharField(blank=True, max_length=60, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
