# Generated by Django 3.2 on 2021-05-02 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myblog', '0011_delete_comments_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('Username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
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
            ],
        ),
    ]