# Generated by Django 4.1.3 on 2022-12-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0003_alter_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]