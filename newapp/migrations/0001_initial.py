# Generated by Django 4.1.7 on 2023-03-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addcategorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(blank=True, max_length=70, null=True)),
                ('image', models.ImageField(upload_to='profile')),
                ('description', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]
