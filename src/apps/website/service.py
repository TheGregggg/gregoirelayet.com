from .models import SkillCategory


async def get_all_skills_categories() -> list[SkillCategory]:
    categories = []
    async for category in SkillCategory.objects.order_by(
        "category_order"
    ).prefetch_related("skill"):
        categories.append(category)

    return categories
