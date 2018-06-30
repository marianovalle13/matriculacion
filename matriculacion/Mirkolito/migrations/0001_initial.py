# Generated by Django 2.0.6 on 2018-06-30 22:24

import Mirkolito.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=30, verbose_name='Materia')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='MatriculacionAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=Mirkolito.models.Curso, related_name='matriculasAlumnos', to='Mirkolito.Curso')),
            ],
            options={
                'verbose_name': 'Matricula de Alumno',
                'verbose_name_plural': 'Matriculas de Alumnos',
            },
        ),
        migrations.CreateModel(
            name='MatriculacionProfesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=Mirkolito.models.Curso, related_name='matriculasProfesores', to='Mirkolito.Curso')),
            ],
            options={
                'verbose_name': 'Matricula Profesor',
                'verbose_name_plural': 'Matricula de Profesores',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.PositiveIntegerField(verbose_name='Nota')),
                ('curso', models.ForeignKey(on_delete=Mirkolito.models.Curso, to='Mirkolito.Curso')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('telefono', models.CharField(max_length=90, verbose_name='Telefono')),
                ('dni', models.PositiveIntegerField(verbose_name='D.N.I')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesor',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Mirkolito.Persona')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
            bases=('Mirkolito.persona',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Mirkolito.Persona')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesor',
            },
            bases=('Mirkolito.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nota',
            name='alumno',
            field=models.ForeignKey(on_delete=Mirkolito.models.Alumno, to='Mirkolito.Alumno'),
        ),
        migrations.AddField(
            model_name='matriculacionprofesor',
            name='profesor',
            field=models.OneToOneField(on_delete=Mirkolito.models.Profesor, related_name='matricula', to='Mirkolito.Profesor'),
        ),
        migrations.AddField(
            model_name='matriculacionalumno',
            name='alumno',
            field=models.OneToOneField(on_delete=Mirkolito.models.Alumno, related_name='matricula', to='Mirkolito.Alumno'),
        ),
    ]
