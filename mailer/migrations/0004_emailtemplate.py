# Generated by Django 3.2.6 on 2021-08-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0003_auto_20210813_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Имя шаблона')),
                ('link', models.CharField(max_length=20, verbose_name='Адрес шаблона')),
            ],
        ),
    ]
