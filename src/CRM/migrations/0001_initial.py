# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(null=True, blank=True)),
                ('address1', models.CharField(max_length=200, null=True, blank=True)),
                ('address2', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=200, null=True, blank=True)),
                ('country', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200, null=True, blank=True)),
                ('address2', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=200, null=True, blank=True)),
                ('country', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=200, null=True, blank=True)),
                ('email', models.EmailField(max_length=200, null=True, blank=True)),
                ('company', models.ForeignKey(blank=True, to='CRM.Company', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(help_text=b'how much this opportunity is worth')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, to='CRM.Company', null=True)),
                ('contact', models.ForeignKey(to='CRM.Contact')),
                ('source', models.ForeignKey(to='CRM.Campaign')),
            ],
            options={
                'verbose_name_plural': 'opportunites',
            },
        ),
        migrations.CreateModel(
            name='OpportunityStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('opportunity', models.ForeignKey(to='CRM.Opportunity')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('opportunity', models.ForeignKey(to='CRM.Opportunity')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField(help_text=b'The order displayed on the screen')),
                ('description', models.TextField(null=True, blank=True)),
                ('value', models.IntegerField(help_text=b'On a scale of 0 to 100')),
            ],
        ),
        migrations.AddField(
            model_name='opportunitystage',
            name='stage',
            field=models.ForeignKey(to='CRM.Stage'),
        ),
        migrations.AddField(
            model_name='opportunitystage',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='stage',
            field=models.ForeignKey(to='CRM.Stage'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='calllog',
            name='opportunity',
            field=models.ForeignKey(to='CRM.Opportunity'),
        ),
        migrations.AddField(
            model_name='calllog',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
