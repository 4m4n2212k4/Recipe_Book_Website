# Generated by Django 4.2.6 on 2023-11-06 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_blog_newblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]