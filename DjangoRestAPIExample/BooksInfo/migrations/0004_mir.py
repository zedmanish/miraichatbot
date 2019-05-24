# Generated by Django 2.0.6 on 2019-05-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksInfo', '0003_authuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=128)),
                ('userid', models.IntegerField()),
                ('currentstate', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'mir',
                'managed': False,
            },
        ),
    ]
