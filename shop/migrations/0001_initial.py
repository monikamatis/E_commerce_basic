# Generated by Django 4.1.5 on 2023-01-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First name.', max_length=100)),
                ('last_name', models.CharField(help_text='Last name.', max_length=100)),
                ('email', models.EmailField(help_text='Please type in your email.', max_length=100)),
                ('password', models.CharField(default=None, help_text='Minimum length 8 characters', max_length=100)),
                ('phone', models.CharField(help_text='Contact number', max_length=10)),
                ('newsletter', models.BooleanField(default=True, help_text='Sign up for our newsletter')),
            ],
        ),
    ]