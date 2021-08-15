from django.db import models


class Email(models.Model):
    email = models.EmailField(
        'Почта',
        unique=True,
    )
    name = models.CharField(
        'Имя',
        max_length=20,
        blank=True
    )
    surname = models.CharField(
        'Фамилия',
        max_length=20,
        blank=True
    )
    birth_date = models.DateField(
        'День рождения',
        blank=True
    )

    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'База E-mail'

    def __str__(self):
        return self.email


class EmailTemplate(models.Model):
    title = models.CharField(
        'Имя шаблона',
        max_length=50,
    )
    link = models.CharField(
        'Адрес шаблона',
        max_length=20,
    )
    subject = models.CharField(
        'Тема письма',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Шаблон письма'
        verbose_name_plural = 'Шаблоны письма'

    def __str__(self):
        return self.title


class SentEmail(models.Model):
    email = models.ForeignKey(
        Email,
        on_delete=models.CASCADE,
        related_name='sends',
        verbose_name='Почта',
    )
    template = models.ForeignKey(
        EmailTemplate,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sends_emails',
        verbose_name='Шаблон',
    )
    send_date = models.DateTimeField(
        'Время отправки',
        auto_now_add=True,
    )
    is_read = models.BooleanField(
        'Прочитано',
        default=False,
    )

    class Meta:
        verbose_name = 'Отправленное письмо'
        verbose_name_plural = 'Отправленные письма'
        ordering = ['-send_date']

    def __str__(self):
        email = self.email
        send_date = self.send_date
        return f'{email}-{send_date}'
