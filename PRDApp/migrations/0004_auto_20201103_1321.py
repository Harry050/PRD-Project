# Generated by Django 3.1.2 on 2020-11-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRDApp', '0003_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
