# Generated by Django 3.2.6 on 2021-08-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0002_rename_sent_mail_sentmail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Почта', 'verbose_name_plural': 'База E-mail'},
        ),
        migrations.AlterField(
            model_name='email',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='День рождения адресата'),
        ),
        migrations.AlterField(
            model_name='email',
            name='name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Имя адресата'),
        ),
        migrations.AlterField(
            model_name='email',
            name='surname',
            field=models.CharField(blank=True, max_length=20, verbose_name='Фамилия адресата'),
        ),
        migrations.AlterField(
            model_name='sentmail',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='Прочитано'),
        ),
    ]
