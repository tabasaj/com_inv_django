# Generated by Django 4.2.11 on 2024-05-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_involvement', '0005_alter_donation_donated'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donated', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=150)),
                ('donation_type', models.CharField(max_length=10)),
                ('gcash_number', models.CharField(max_length=11)),
                ('paymaya_number', models.CharField(max_length=11)),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('address_volunteer', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=11)),
                ('date_sched', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
