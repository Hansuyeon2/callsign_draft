# Generated by Django 4.1.2 on 2022-10-09 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count',
            field=models.CharField(max_length=30, null='True'),
            preserve_default='True',
        ),
    ]
