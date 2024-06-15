from wagtail.test.utils import WagtailPageTestCase
from wagtail.rich_text import RichText
from wagtail.models import Page, Site
from .models import HomePage

from apps.project.models import ProjectsPage, ProjectPage


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
        cls.home = HomePage(title="Home", about_me=RichText("<p>About me text</p>"))
        root.add_child(instance=cls.home)

        projects = ProjectsPage(title="Projects")
        one_project = ProjectPage(
            title="Test Project",
            description=RichText("<p>project description</p>"),
            show_on_home_page=True,
        )
        cls.home.add_child(instance=projects)
        projects.add_child(instance=one_project)

    def test_get(self):
        response = self.client.get(self.home.url)
        self.assertEqual(response.status_code, 200)

    def test_default_route_rendering(self):
        self.assertPageIsRenderable(self.home)

    def test_page_content(self):
        response = self.client.get(self.home.url)
        self.assertContains(response, "Grégoire Layet")
        self.assertContains(response, "About me text")
        self.assertContains(response, "Test Project")
        self.assertContains(response, "project description")
