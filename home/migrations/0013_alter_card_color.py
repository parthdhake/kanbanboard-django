# Generated by Django 3.2.7 on 2021-09-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_card_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('white', 'WHITE'), ('red', 'RED'), ('green', 'GREEN')], default='white', max_length=6),
        ),
    ]
