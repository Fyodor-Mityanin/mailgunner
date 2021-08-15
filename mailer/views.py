import os

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from .forms import EmailForm, SentEmailForm
from .models import Email, SentEmail
from .tasks import send_emails

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


@login_required
def index(request):
    form = SentEmailForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        template_id = form.instance.template.pk
        time = form.cleaned_data['time_of_sending']
        send_emails(template_id, time)
        return redirect('mailer:index')
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
    dir = os.path.dirname(os.path.abspath(__file__))
    image = open(os.path.join(dir, 'static/pixel.png'), 'rb').read()
    email = SentEmail.objects.get(pk=pk)
    email.is_read = True
    email.save()
    return HttpResponse(image, content_type="image/png")
