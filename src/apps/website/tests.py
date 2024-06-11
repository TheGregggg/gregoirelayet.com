from wagtail.test.utils import WagtailPageTestCase
from wagtail.models import Page, Site
from .models import HomePage


# Create your tests here.
class HomePageTests(WagtailPageTestCase):
    @classmethod
    def setUpTestData(cls):
        root = Page.get_first_root_node()
        assert root

        Site.objects.create(
            hostname="test_site",
            root_page=root,
            is_default_site=True,
            site_name="test_site",
        )
        cls.home = HomePage(title="Home")
        root.add_child(instance=cls.home)

    def test_get(self):
        response = self.client.get(self.home.url)
        self.assertEqual(response.status_code, 200)

    def test_default_route(self):
        self.assertPageIsRoutable(self.home)

    def test_default_route_rendering(self):
        self.assertPageIsRenderable(self.home)

    def test_page_content(self):
        response = self.client.get(self.home.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Grégoire Layet")
