# Generated by Django 2.2.6 on 2019-12-24 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191209_0314'),
        ('pennychat', '0002_followup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follow_ups', to='users.UserProfile'),  # noqa
        ),
        migrations.AlterField(
            model_name='pennychat',
            name='user',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Organizer'), (2, 'Attendee'), (3, 'Invitee')], default=3)),
                ('penny_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='pennychat.PennyChat')),  # noqa
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='users.UserProfile')),  # noqa
            ],
            options={
                'unique_together': {('penny_chat', 'user')},
            },
        ),
    ]
