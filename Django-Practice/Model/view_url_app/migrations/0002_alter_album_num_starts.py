# Generated by Django 3.2.6 on 2021-08-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_url_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_starts',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Worsted'), (3, 'nice'), (4, 'Like'), (5, 'Wow')]),
        ),
    ]
