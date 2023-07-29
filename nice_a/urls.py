from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from nice_a import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nice_a.common.urls')),
    path('accounts/', include('nice_a.accounts.urls')),
    path('pets/', include('nice_a.pets.urls')),
    path('photos/', include('nice_a.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
