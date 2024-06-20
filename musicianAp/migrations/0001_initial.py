# Generated by Django 5.0.6 on 2024-06-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('Instrument_Type', models.CharField(choices=[('Grid', 'Grid'), ('Flute', 'Flute'), ('Piano', 'Piano'), ('Trumpet', 'Trumpet'), ('Banjo', 'Banjo')], max_length=10)),
            ],
        ),
    ]
