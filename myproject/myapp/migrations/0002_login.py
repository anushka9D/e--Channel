# Generated by Django 5.1.3 on 2024-11-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('email', models.EmailField(editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('user_role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10)),
            ],
        ),
    ]
