import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

# DB
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')

# Redis
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')

# Домен (ip) при развертывании на сервере
DOMEN_HOSTS = env('DOMEN_HOSTS').split(', ')

# Статусы для мягкого удаления записей
STATUS_CHOICES = [
    (True, 'Удалено'),
    (False, 'Активно'),
]
