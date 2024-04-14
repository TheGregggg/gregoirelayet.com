from django.contrib import admin

from apps.website.models import SkillCategory
from apps.website.admin import SkillCategoryAdmin


class GregAdmin(admin.AdminSite):
    site_header = "Greg's Admin"
    site_title = "Greg's Admin"

    login_template = "registration/login.html"


admin_site = GregAdmin(name="greg_admin")


admin_site.register(SkillCategory, SkillCategoryAdmin)
