import os
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from .forms import EmailForm, SentEmailForm
from .models import Email, EmailTemplate, SentEmail
from .tasks import send_emails

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


def get_message_text(time=None):
    if time is None:
        return 'Сообщения отправлены'
    return f'Сообщения будут отправлены {time}'


@login_required
def index(request):
    form = SentEmailForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        template_id = form.instance.template.pk
        time = form.cleaned_data['time_of_sending']
        send_emails.delay(template_id, time)
        text = get_message_text(time)
        return render(request, 'message.html', {'text': text, })
    return render(request, 'index.html', {'form': form, })


@login_required
def emails(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mailer:emails')
    emails_list = Email.objects.all()
    paginator = Paginator(emails_list, 30)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'emails.html',
        {'page': page, 'paginator': paginator, 'form': form, }
    )


@login_required
def sent_emails(request):
    sent_emails_list = SentEmail.objects.all()
    paginator = Paginator(sent_emails_list, 30)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'sent_emails.html',
        {'page': page, 'paginator': paginator}
    )


def tracking(request, pk):
    dir = Path(__file__).resolve().parent
    image = open(os.path.join(dir, 'static/pixel.PNG'), 'rb').read()
    email = SentEmail.objects.get(pk=pk)
    email.is_read = True
    email.save()
    return HttpResponse(image, content_type="image/png")


@login_required
def templates(request):
    templates = EmailTemplate.objects.all()
    return render(request, 'templates.html', {'templates': templates})
