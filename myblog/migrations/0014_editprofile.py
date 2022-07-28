# Generated by Django 3.2 on 2021-05-02 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0013_delete_editprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('profilepic', models.ImageField(null=True, upload_to='')),
                ('bio', models.TextField(null=True)),
                ('number', models.CharField(max_length=10, null=True)),
                ('section', models.CharField(max_length=1, null=True)),
                ('branch', models.CharField(max_length=10, null=True)),
                ('year', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('instagram_link', models.CharField(max_length=300, null=True)),
                ('facebook_link', models.CharField(max_length=300, null=True)),
                ('linkedin_link', models.CharField(max_length=300, null=True)),
                ('Username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]