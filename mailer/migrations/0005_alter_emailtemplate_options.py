# Generated by Django 3.2.6 on 2021-08-14 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0004_emailtemplate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'verbose_name': 'Шаблон письма', 'verbose_name_plural': 'Шаблоны письма'},
        ),
    ]