from .lang_switcher import Lang_switcher
from django.test import TestCase
from django.conf import settings
from django.utils.translation import get_language_info


class LangSwitcherTestCase(TestCase):
    def test_rendering(self):
        try:
            Lang_switcher.render()
        except:
            self.fail("Lang_switcher can't render")

    def test_lang_present_in_dorpdown(self):
        render = Lang_switcher.render()
        for lang_code, _ in settings.LANGUAGES:
            lang_name_local = get_language_info(lang_code)["name_local"].capitalize()
            self.assertTrue(f'value="{lang_name_local}"' in render)
