# Generated by Django 2.1 on 2019-12-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
