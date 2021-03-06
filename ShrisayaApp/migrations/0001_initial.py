# Generated by Django 3.2.4 on 2021-09-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('cotact_id', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('fname', models.CharField(db_column='fname', max_length=70)),
                ('lname', models.CharField(db_column='lname', max_length=70)),
                ('email', models.EmailField(db_column='email', max_length=70)),
                ('phn', models.BigIntegerField(db_column='phn')),
                ('message', models.CharField(db_column='message', max_length=1000)),
            ],
            options={
                'db_table': 'cotact_form',
            },
        ),
    ]
