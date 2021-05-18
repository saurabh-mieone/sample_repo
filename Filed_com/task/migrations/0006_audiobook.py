# Generated by Django 3.2 on 2021-05-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_delete_audiobook'),
    ]

    operations = [
        migrations.CreateModel(
            name='audiobook',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=' ', max_length=100)),
                ('author', models.CharField(default=' ', max_length=100)),
                ('narrator', models.CharField(default=' ', max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('upload_time', models.DateTimeField()),
            ],
        ),
    ]
