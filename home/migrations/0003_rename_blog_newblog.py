# Generated by Django 4.2.6 on 2023-11-06 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='NewBlog',
        ),
    ]