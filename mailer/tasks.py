import os
from time import sleep

from celery import shared_task
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from dotenv import load_dotenv

from .models import Email, SentEmail, EmailTemplate

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


def get_html_emails(template):
    emails = Email.objects.all()
    email_objects = []
    for email in emails:
        sent_email_pk = create_sent_email(email, template)
        subject, from_email, to = template.subject, EMAIL_HOST_USER, email.email
        t = loader.get_template(template.link)
        data = {
            'name': email.name,
            'surname': email.surname,
            'birth_date': email.birth_date,
            'sent_email_pk': sent_email_pk,
        }
        html_content = t.render(data)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.content_subtype = 'html'
        email_objects.append(msg)
    return email_objects


def create_sent_email(email, template):
    sent_email = SentEmail(email=email, template=template)
    sent_email.save()
    return sent_email.pk


@shared_task
def send_emails(template_id, time=None):
    template = EmailTemplate.objects.get(id=template_id)
    if time is not None:
        sleep(30)
        print('We slept 30 sec')
    connection = mail.get_connection()
    try:
        messages = get_html_emails(template)
        connection.send_messages(messages)
    except:
        pass
    return None
