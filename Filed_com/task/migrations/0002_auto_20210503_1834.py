# Generated by Django 3.2 on 2021-05-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Class',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='Name',
            field=models.CharField(default='', max_length=10),
        ),
    ]