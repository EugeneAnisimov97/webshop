# Generated by Django 5.1.4 on 2024-12-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('content', models.TextField(max_length=100, verbose_name='Content')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('time_update', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
