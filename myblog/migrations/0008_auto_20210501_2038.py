# Generated by Django 3.2 on 2021-05-01 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_rename_username_comments_section_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_username',
        ),
        migrations.DeleteModel(
            name='comments_section',
        ),
        migrations.DeleteModel(
            name='reply',
        ),
    ]
