from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel


@register_setting
class Header(BaseGenericSetting):
    pages = StreamField([("Page", blocks.PageChooserBlock(can_choose_root=True))])

    panels = [
        FieldPanel("pages"),
    ]
