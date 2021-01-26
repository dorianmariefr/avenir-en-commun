# Generated by Django 3.1.4 on 2021-01-26 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('number', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('number', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.chapter')),
            ],
        ),
    ]