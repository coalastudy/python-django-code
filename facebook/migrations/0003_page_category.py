# Generated by Django 2.0.4 on 2018-06-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.CharField(default='', max_length=120),
        ),
    ]