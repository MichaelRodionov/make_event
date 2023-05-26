from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from make_event import settings

# ----------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('core.urls')),
    path('org/', include('organizations.urls')),
    path('event/', include('events.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# ----------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
