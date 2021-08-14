from django.urls import path

from . import views

app_name = 'mailer'

urlpatterns = [
    path('', views.index, name='index'),
    path('sent_emails/', views.sent_emails, name='sent_emails'),
]
