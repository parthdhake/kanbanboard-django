# Generated by Django 3.2.7 on 2021-09-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
