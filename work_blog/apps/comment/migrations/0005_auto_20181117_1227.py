# Generated by Django 2.1.1 on 2018-11-17 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20181116_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_time'], 'verbose_name': '评论内容', 'verbose_name_plural': '评论内容'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='comment.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='给()回复'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_comment', to='comment.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
    ]
