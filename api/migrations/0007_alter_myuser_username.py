# Generated by Django 3.2.13 on 2023-01-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='25f71989-3dfc-47b2-8c6d-d40d6dba3ad9', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
