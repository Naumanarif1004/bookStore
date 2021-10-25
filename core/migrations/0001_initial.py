# Generated by Django 3.2.8 on 2021-10-25 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('synopsis', models.CharField(blank=True, max_length=165, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
