from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import HomeView, StoreView, OrderSummaryView, ItemDetailView


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('core:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_store_url_is_resolved(self):
        url = reverse('core:store')
        self.assertEquals(resolve(url).func.view_class, StoreView)

    def test_order_summary_url_is_resolved(self):
        url = reverse('core:order-summary')
        self.assertEquals(resolve(url).func.view_class, OrderSummaryView)

    def test_product_url_is_resolved(self):
        url = reverse('core:product', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, ItemDetailView)
