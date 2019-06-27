# Generated by Django 2.2.2 on 2019-06-27 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Extra_classe', '0010_auto_20190627_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='data',
            field=models.DateField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='disciplina',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Extra_classe.Disciplina'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='hora',
            field=models.TimeField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='nome_professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Extra_classe.Profdisciplina'),
            preserve_default=False,
        ),
    ]