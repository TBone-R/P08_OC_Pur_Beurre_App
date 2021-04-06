from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model


class TestPasswordChange(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Edge('functional_tests/msedgedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_home_page(self):

        self.browser.get(self.live_server_url + '/register/')

        email_box = self.browser.find_element_by_name("email")

        email_box.send_keys("testuser@mail.com")

        user_box = self.browser.find_element_by_name("username")

        user_box.send_keys("testuser")

        new_pass_box1 = self.browser.find_element_by_name("password1")

        new_pass_box1.send_keys("vi19sa96&*")

        new_pass_box2 = self.browser.find_element_by_name("password2")

        new_pass_box2.send_keys("vi19sa96&*")

        new_pass_box2.send_keys(Keys.ENTER)

        email_box = self.browser.find_element_by_name("username")

        email_box.send_keys("testuser@mail.com")

        pass_box = self.browser.find_element_by_name("password")

        pass_box.send_keys("vi19sa96&*")

        pass_box.send_keys(Keys.ENTER)

        self.browser.get(self.live_server_url + '/password/')

        old_pass_box = self.browser.find_element_by_name("old_password")

        old_pass_box.send_keys("vi19sa96&*")

        new_pass_box1 = self.browser.find_element_by_name("new_password1")

        new_pass_box1.send_keys("vi19sa96&*v2")

        new_pass_box2 = self.browser.find_element_by_name("new_password2")

        new_pass_box2.send_keys("vi19sa96&*v2")

        new_pass_box2.send_keys(Keys.ENTER)

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/myaccount/'
        )

