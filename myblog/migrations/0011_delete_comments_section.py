# Generated by Django 3.2 on 2021-05-01 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_alter_comments_section_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comments_section',
        ),
    ]
