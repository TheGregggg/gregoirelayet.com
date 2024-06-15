from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
import os

from config.admin import admin_site

urlpatterns = [
    path("superadmin/", admin_site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += (
        staticfiles_urlpatterns()
    )  # tell gunicorn where static files are in dev mode
    urlpatterns += static(
        settings.MEDIA_URL + "images/",
        document_root=os.path.join(settings.MEDIA_ROOT, "images"),
    )
