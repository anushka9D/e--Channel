# Generated by Django 5.1.3 on 2024-12-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='user_role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('nurse', 'Nurse'), ('support_staff', 'Support_staff'), ('doctor', 'Doctor')], default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('nurse', 'Nurse'), ('support_staff', 'Support_staff'), ('doctor', 'Doctor')], default='user', max_length=100),
        ),
    ]
