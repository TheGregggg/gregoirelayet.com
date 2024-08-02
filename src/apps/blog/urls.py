from django.urls import path

from .tags import autocomplete

urlpatterns = [
    path(
        "admin/tag-autocomplete/<slug:app_name>/<slug:model_name>/",
        autocomplete,
        name="wagtailadmin_tag_model_autocomplete",
    ),
]
