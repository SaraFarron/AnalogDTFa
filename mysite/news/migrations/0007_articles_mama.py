# Generated by Django 3.0.8 on 2020-08-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_articles_lol'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='mama',
            field=models.IntegerField(default=1000),
        ),
    ]
