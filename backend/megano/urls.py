from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='API для интернет-магазина Megano',
        default_version='v1',
        description='Описание роутов для выполнения запросов к API',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='admin@megano.ru'),
        license=openapi.License(name=''),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('api/', include([
        path('profile/', include('backend.user_profile.urls')),
    ])),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]

if settings.DEBUG:
    # Обслуживание медиа-файлов
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    )

    # Вывод статических файлов
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

# Переопределяем шапку в админке
admin.site.site_header = 'Админка Megano'
