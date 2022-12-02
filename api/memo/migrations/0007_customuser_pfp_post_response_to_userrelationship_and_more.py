# Generated by Django 4.1.3 on 2022-12-02 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0006_remove_post_id_post_dislike_post_like_post_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pfp',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='response_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='memo.post'),
        ),
        migrations.CreateModel(
            name='UserRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permission_type', to='memo.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_permission', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]