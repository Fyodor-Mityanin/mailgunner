from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('users.urls', namespace='users')),
    path('', include('mailer.urls', namespace='mailer')),
]
