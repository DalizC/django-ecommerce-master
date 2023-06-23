from django.test import TestCase
from core.models import Item


class TestModels(TestCase):

    def setUp(self):
        self.item1 = Item.objects.create(
            title='item1',
            price=1990,
            description='some description'
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertAlmostEquals(self.item1.slug, 'item1')
