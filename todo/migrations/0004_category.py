# Generated by Django 3.1.2 on 2020-11-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]