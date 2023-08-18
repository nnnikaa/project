from .views import index, top_sellers, register
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'main-page'),
    path('top-sellers', top_sellers, name = 'top-sellers'),
    path('register', register, name = 'register')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)