# Generated by Django 2.2.2 on 2019-06-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra_classe', '0009_auto_20190627_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='Confirmar',
            field=models.BooleanField(default=True),
        ),
    ]