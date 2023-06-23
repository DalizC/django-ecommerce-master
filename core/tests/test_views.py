from django.test import TestCase, Client
from django.urls import reverse
from core.models import Item


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('core:home')
        self.store = reverse('core:store')
        self.order_summary = reverse('core:order-summary')
        self.item1 = self.product = reverse('core:product', args=['item1'])
        Item.objects.create(
            title='item1',
            price=1990,
            description='some description'
        )

    def test_project_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_project_store_GET(self):
        response = self.client.get(self.store)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store.html')

    def test_project_order_summary_GET(self):
        response = self.client.get(self.order_summary)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order-summary.html')

    def test_project_product_GET(self):
        response = self.client.get(self.product)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')
