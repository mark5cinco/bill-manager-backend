# Generated by Django 2.2.3 on 2019-07-14 09:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventuser',
            unique_together={('user', 'event')},
        ),
    ]
