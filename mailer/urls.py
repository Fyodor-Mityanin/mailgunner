from django.urls import path

from . import views

app_name = 'mailer'

urlpatterns = [
    path('', views.index, name='index'),
    path('emails/', views.emails, name='emails'),
    path('message/', views.message, name='message'),
    path('sent_emails/', views.sent_emails, name='sent_emails'),
    path('tracking/<int:pk>/', views.tracking, name='tracking')
]