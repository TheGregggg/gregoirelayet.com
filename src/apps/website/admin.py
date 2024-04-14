from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


class SkillCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [SkillInline]
