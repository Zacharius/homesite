# Generated by Django 2.0.3 on 2018-04-16 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180415_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='htmlFile',
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default='Hello World'),
            preserve_default=False,
        ),
    ]
