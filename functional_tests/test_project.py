from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestProject(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Edge('functional_tests/msedgedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_home_page(self):

        self.browser.get(self.live_server_url)

        home_title = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(
            home_title,
            "DU GRAS, OUI, MAIS DE QUALITÉ !"
        )

