# Generated by Django 3.0.8 on 2020-08-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_articles_mama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='mama',
            field=models.IntegerField(default=100),
        ),
    ]