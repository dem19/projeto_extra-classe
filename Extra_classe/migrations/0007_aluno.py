# Generated by Django 2.2.2 on 2019-06-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra_classe', '0006_auto_20190626_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponivel', models.BooleanField(default=False)),
            ],
        ),
    ]
