# Generated by Django 5.0 on 2024-01-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_create', models.DateTimeField(auto_now=True)),
                ('is_complected', models.BooleanField(default=False)),
            ],
        ),
    ]
