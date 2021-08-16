# Generated by Django 3.2.6 on 2021-08-13 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('name', models.CharField(max_length=20, verbose_name='Имя адресата')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия адресата')),
                ('birth_date', models.DateTimeField(blank=True, verbose_name='День рождения адресата')),
            ],
            options={
                'verbose_name': 'Почта',
            },
        ),
        migrations.CreateModel(
            name='Sent_mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')),
                ('is_read', models.CharField(max_length=20, verbose_name='Имя адресата')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sends', to='mailer.email', verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Отправленное письмо',
                'verbose_name_plural': 'Отправленные письма',
            },
        ),
    ]