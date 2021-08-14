from django.db import models

class Email(models.Model):
    email = models.EmailField(
        'Почта',
        unique=True,
    )
    name = models.CharField(
        'Имя адресата',
        max_length=20,
        blank=True
    )
    surname = models.CharField(
        'Фамилия адресата',
        max_length=20,
        blank=True
    )
    birth_date = models.DateField(
        'День рождения адресата',
        blank=True
    )
    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'База E-mail'

    def __str__(self):
        return self.email

class SentMail(models.Model):
    email = models.ForeignKey(
        Email,
        on_delete=models.CASCADE,
        related_name='sends',
        verbose_name='Почта',
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

    def __str__(self):
        email = self.email
        send_date = self.send_date
        return f'{email}-{send_date}'