# Generated by Django 4.0.3 on 2022-04-06 08:46

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
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('foreman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Бригадир')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Оклад')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('degree', models.IntegerField(default=3, verbose_name='Разряд')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salary.department', verbose_name='Участок')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salary.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.JSONField(null=True, verbose_name='Числа')),
                ('dataSheet', models.DateField(default='2022-04-06', verbose_name='Дата')),
                ('foreman', models.CharField(max_length=50, verbose_name='Бригадир')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salary.department', verbose_name='Участок')),
            ],
            options={
                'verbose_name': 'Табель',
                'verbose_name_plural': 'Табеля',
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Статус')),
                ('Note', models.TextField(max_length=500, verbose_name='Примечание')),
                ('name_director', models.CharField(max_length=50, verbose_name='Начальник производства')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salary.department', verbose_name='Участок')),
                ('time_sheet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salary.timesheet', verbose_name='Табель')),
            ],
            options={
                'verbose_name': 'Расчетный лист',
                'verbose_name_plural': 'Расчетные листы',
            },
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Наименование')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('dtc', models.CharField(max_length=50, verbose_name='ОТК')),
                ('status', models.BooleanField(verbose_name='Статус')),
                ('fine_date', models.DateField(auto_now_add=True, verbose_name='Дата штрафа')),
                ('note', models.TextField(max_length=500, verbose_name='Примечание')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salary.worker', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Штраф',
                'verbose_name_plural': 'Штрафы',
                'ordering': ['create_date'],
            },
        ),
    ]
