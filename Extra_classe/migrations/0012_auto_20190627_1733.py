# Generated by Django 2.2.2 on 2019-06-27 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Extra_classe', '0011_auto_20190627_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='data',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='nome_professor',
        ),
    ]
