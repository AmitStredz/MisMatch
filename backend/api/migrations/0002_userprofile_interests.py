# Generated by Django 5.1.1 on 2024-10-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
