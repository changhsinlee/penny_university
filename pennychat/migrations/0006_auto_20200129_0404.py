# Generated by Django 2.2.6 on 2020-01-29 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pennychat', '0005_auto_20200120_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_chats', to='users.UserProfile'),  # noqa
        ),
    ]
