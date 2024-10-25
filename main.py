import os
import django
from django.core.management import execute_from_command_line
from django.conf import settings
from django.urls import path
from views import health_check  # Импортируем напрямую из views

# Минимальная настройка конфигурации
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='a-very-secret-key',
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
    ],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
    ],
)

# Указываем маршруты прямо в main.py
urlpatterns = [
    path('healthz', health_check),
]

# Инициализируем Django
django.setup()

# Запускаем сервер
if __name__ == "__main__":
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
