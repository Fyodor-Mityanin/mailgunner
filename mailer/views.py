from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import loader
from django.core import mail
from .forms import SentEmailForm
from .models import Email, SentEmail
import os
from django.core.paginator import Paginator

from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


def get_html_emails(template):
    emails = Email.objects.all()
    email_objects = []
    for email in emails:
        subject, from_email, to = template.subject, EMAIL_HOST_USER, email.email
        t = loader.get_template(template.link)
        data = {'name': email.name,
                'surname': email.surname,
                'birth_date': email.birth_date,
                }
        html_content = t.render(data)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.content_subtype = 'html'
        email_objects.append(msg)
    return email_objects


def create_sent_emails(messages, template):
    objs = [
        SentEmail(
            email=Email.objects.get(email=email.to[0]),
            template=template,
        )
        for email in messages
    ]
    SentEmail.objects.bulk_create(objs)


@login_required
def index(request):
    form = SentEmailForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        template = form.instance.template
        connection = mail.get_connection()
        messages = get_html_emails(template)
        connection.send_messages(messages)
        create_sent_emails(messages, template)
        return redirect('mailer:index')
    return render(request, 'index.html', {'form': form, })


@login_required
def sent_emails(request):
    sent_emails_list = SentEmail.objects.all()
    paginator = Paginator(sent_emails_list, 100)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'sent_emails.html',
        {'page': page, 'paginator': paginator}
    )
