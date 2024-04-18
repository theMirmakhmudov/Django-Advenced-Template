from django.urls import path
from apps.views import index, show_image, test_html, calendar_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('images', show_image),
    path('test', test_html),
    path('calendar', calendar_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
