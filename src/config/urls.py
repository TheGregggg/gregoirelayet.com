from django.urls import path, include

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls

from config.admin import admin_site

urlpatterns = [
    path("superadmin/", admin_site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("", include("apps.website.urls")),
    path("", include(wagtail_urls)),
]

# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#     urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
#     urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
#     urlpatterns += [
#         path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
#     ]
