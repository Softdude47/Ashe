# Generated by Django 2.1 on 2020-01-04 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Profile_Picture',
        ),
    ]
