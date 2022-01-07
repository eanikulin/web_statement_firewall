# Generated by Django 3.2.7 on 2021-12-23 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211215_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='recipient_bid',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='source_bid',
        ),
        migrations.CreateModel(
            name='SourceBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_bid', models.GenericIPAddressField(default='192.168.0.1', verbose_name='Источник')),
                ('bid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.bid')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_bid', models.GenericIPAddressField(default='192.168.0.2', verbose_name='Получатель')),
                ('bid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.bid')),
            ],
        ),
    ]