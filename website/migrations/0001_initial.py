# Generated by Django 5.1.4 on 2024-12-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('deccription', models.CharField(max_length=50)),
                ('cover_image', models.ImageField(default='', upload_to='static/images/')),
            ],
        ),
    ]