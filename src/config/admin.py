from django.contrib import admin


class GregAdmin(admin.AdminSite):
    site_header = "Greg's Admin"
    site_title = "Greg's Admin"

    login_template = "registration/login.html"


admin_site = GregAdmin(name="greg_admin")
