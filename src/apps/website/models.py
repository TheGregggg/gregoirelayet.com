from django.db import models


class SkillCategory(models.Model):
    class Meta:
        ordering = ["category_order"]
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    name = models.CharField(max_length=100)
    category_order = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False, db_index=True
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    class Meta:
        ordering = ["skill_order"]

    text = models.TextField(max_length=300)
    category = models.ForeignKey(
        SkillCategory, related_name="skill", on_delete=models.CASCADE
    )

    skill_order = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False, db_index=True
    )

    def __str__(self):
        return self.text[:50]
