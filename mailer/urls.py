from django.urls import path

from . import views

app_name = 'mailer'

urlpatterns = [
    path('', views.index, name='index')
]
