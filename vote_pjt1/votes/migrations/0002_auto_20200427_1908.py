# Generated by Django 2.1.15 on 2020-04-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pick',
            field=models.CharField(choices=[('Agree', 'Agree'), ('Disagree', 'Disagree')], default='Agree', max_length=10),
        ),
    ]