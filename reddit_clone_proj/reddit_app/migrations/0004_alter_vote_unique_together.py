# Generated by Django 4.0.1 on 2022-01-26 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_app', '0003_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('post',)},
        ),
    ]
