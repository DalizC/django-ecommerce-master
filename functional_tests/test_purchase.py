from selenium import webdriver
from core.models import Item
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class asdS(StaticLiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.close()
        # return super().tearDown()

    def test_no_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)
