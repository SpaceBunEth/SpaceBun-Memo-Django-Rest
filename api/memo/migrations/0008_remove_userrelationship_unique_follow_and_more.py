# Generated by Django 4.1.3 on 2022-12-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0007_remove_userrelationship_unique_follow_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userrelationship',
            name='unique_follow',
        ),
        migrations.AddConstraint(
            model_name='userrelationship',
            constraint=models.UniqueConstraint(fields=('follower', 'following'), name='unique_follow'),
        ),
    ]
