from django.core.management import call_command

from test_plus.test import TestCase
from wagtail.wagtailcore.models import Page, Site
from wagtail.tests.utils import WagtailPageTests

from cms.models import ClassroomTool


class CMSModelTests(TestCase):

    def setUp(self):
        p = Page()
        p.title='Root Page'
        p.slug='root-page'
        p.depth=0
        p.save()

        s=Site()
        s.root_page=p
        s.is_default_site=True
        s.hostname='localhost'
        s.port=80
        s.save()


    def test_classroom_tool(self):
        """
        Test creation of a Classroom Tool.
        """

        # root_page = Site.objects.get(is_default_site=True).root_page

        t = WagtailPageTests()
        t.assertCanCreateAt(Page, ClassroomTool)
