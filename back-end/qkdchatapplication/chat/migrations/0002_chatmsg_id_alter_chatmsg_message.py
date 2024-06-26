# Generated by Django 5.0.4 on 2024-04-06 18:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmsg',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chatmsg',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]
