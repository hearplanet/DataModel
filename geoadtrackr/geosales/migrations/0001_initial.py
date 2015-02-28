# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=100)),
                ('app_store', models.CharField(max_length=100)),
                ('current_bid', models.IntegerField(default=0)),
                ('app_balance', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='App_to_Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_bid', models.IntegerField(default=0)),
                ('app_id', models.ForeignKey(to='geosales.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Geofield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.DecimalField(max_digits=15, decimal_places=10)),
                ('lon', models.DecimalField(max_digits=15, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Install',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('install_time', models.DateTimeField(verbose_name=b'datetime installed')),
                ('install_bid', models.IntegerField(default=0)),
                ('lat', models.DecimalField(max_digits=15, decimal_places=10)),
                ('lon', models.DecimalField(max_digits=15, decimal_places=10)),
                ('app_id', models.ForeignKey(to='geosales.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue_name', models.CharField(max_length=100)),
                ('agent_id', models.ForeignKey(to='geosales.Agent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='install',
            name='venue',
            field=models.ForeignKey(to='geosales.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geofield',
            name='venue_id',
            field=models.OneToOneField(to='geosales.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='app_to_venue',
            name='venue_id',
            field=models.ForeignKey(to='geosales.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='app',
            name='publisher',
            field=models.ForeignKey(to='geosales.Publisher'),
            preserve_default=True,
        ),
    ]
