# Generated by Django 4.2.5 on 2023-09-07 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='messahe',
            new_name='message',
        ),
    ]
