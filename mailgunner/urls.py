from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('users.urls', 'users'), namespace='users')),
    path('', include(('mailer.urls', 'mailer'), namespace='mailer')),
]
