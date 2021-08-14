from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import LoginForm


class Login(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('mailer:index')
    template_name = 'users/login.html'
