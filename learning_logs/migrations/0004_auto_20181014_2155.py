# Generated by Django 2.1.2 on 2018-10-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20181014_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='create_date',
            new_name='date_added',
        ),
    ]