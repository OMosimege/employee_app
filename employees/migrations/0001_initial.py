# Generated by Django 4.2.18 on 2025-01-19 09:05

from django.db import migrations, models
import django.db.models.deletion
import employees.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(default=employees.models.generate_employee_id, editable=False, max_length=6, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_experience', models.CharField(choices=[('1', '1 Year'), ('2', '2 Years'), ('3', '3 Years'), ('4', '4 Years'), ('5+', '5+ Years')], max_length=3)),
                ('seniority_rating', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=12)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.skill')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(through='employees.EmployeeSkill', to='employees.skill'),
        ),
    ]
