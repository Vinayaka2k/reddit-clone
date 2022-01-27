# Generated by Django 4.0.1 on 2022-01-26 18:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit_app', '0004_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'post')},
        ),
    ]
