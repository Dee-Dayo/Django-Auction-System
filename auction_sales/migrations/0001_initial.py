# Generated by Django 5.0.6 on 2024-06-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('S', 'SELLER'), ('B', 'BIDDER')], max_length=1)),
                ('is_logged_in', models.BooleanField(default=False)),
            ],
        ),
    ]
