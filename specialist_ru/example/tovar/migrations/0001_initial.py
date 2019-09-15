# Generated by Django 2.2.5 on 2019-09-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('article', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=126, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
