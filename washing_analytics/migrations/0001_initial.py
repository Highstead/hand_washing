# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('geo_lat', models.FloatField(null=True, blank=True)),
                ('geo_lng', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=2048)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GUIDModel',
            fields=[
                ('guid', models.CharField(max_length=40, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('guidmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='washing_analytics.GUIDModel')),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 11, 22, 21, 45, 22, 89140))),
                ('duration', models.FloatField(default=0.0)),
                ('status', models.CharField(max_length=1, choices=[(0, b'Wash'), (1, b'WiiBoard')])),
            ],
            options={
            },
            bases=('washing_analytics.guidmodel',),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.ForeignKey(to='washing_analytics.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=2048)),
                ('division', models.ForeignKey(to='washing_analytics.Division')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamReduce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete', models.IntegerField()),
                ('washed', models.IntegerField()),
                ('unwashed', models.IntegerField()),
                ('timespent', models.FloatField()),
                ('division', models.ForeignKey(to='washing_analytics.Division')),
                ('team', models.ForeignKey(to='washing_analytics.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(to='washing_analytics.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='teams',
            field=models.ManyToManyField(to='washing_analytics.Team', through='washing_analytics.Membership'),
            preserve_default=True,
        ),
    ]
