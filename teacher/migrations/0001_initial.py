# Generated by Django 4.1 on 2022-08-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('T_ID', models.CharField(default='16201519-001', max_length=12, primary_key=True, serialize=False)),
                ('T_name', models.CharField(default='', max_length=50)),
                ('T_gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='M', max_length=1)),
                ('T_class', models.CharField(default='', max_length=50)),
            ],
        ),
    ]