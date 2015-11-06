# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.IntegerField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.IntegerField(serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Publisher', models.CharField(max_length=30)),
                ('PublishDate', models.DateField()),
                ('Price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('AuthorID', models.ForeignKey(to='books.Author')),
            ],
        ),
    ]
