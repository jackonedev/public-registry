from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home, readme


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('readme/', readme, name='readme'),
    path('app/', include('application.urls'), name='app'),

    # REST FRAMEWORK URLS
    path('api/v1/', include('application.api.urls', namespace='app_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)