# Generated by Django 2.1 on 2019-03-13 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ('-published_at',), 'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolios'},
        ),
    ]