from wagtail.models import Page, Site
from wagtail.rich_text import RichText
from wagtail.test.utils import WagtailPageTestCase

from apps.project.models import ProjectPage, ProjectsPage

from .models.homepage import HomePage


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
        project_one = ProjectPage(
            title="Test Project",
            short_description=RichText("<p>project description</p>"),
            description=RichText("<p>project complete description</p>"),
            show_on_home_page=True,
        )
        project_two = ProjectPage(
            title="invisible_on_home_page_project",
            short_description=RichText(
                "<p>project_short_description_should_be_visible</p>"
            ),
            description=RichText("<p>project_description_should_be_visible</p>"),
            show_on_home_page=False,
        )
        cls.home.add_child(instance=projects)
        projects.add_child(instance=project_one)
        projects.add_child(instance=project_two)

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

        self.assertNotContains(response, "invisible_on_home_page_project")
        self.assertNotContains(response, "project_description_should_be_visible")
