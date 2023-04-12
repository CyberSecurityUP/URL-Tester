# Generated by Django 3.2.10 on 2023-04-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('status_code', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
