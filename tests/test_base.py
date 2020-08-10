import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class TestBase(unittest.TestCase):
    """
    Home page tests
    """
    PageClass = None

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options,
                                        executable_path='./geckodriver')
        self.page = self.PageClass(self.driver)
        self.driver.get(self.page.page_url)
        self.driver.maximize_window()
        self.page.is_browser_on_page()

    def tearDown(self):
        """
        Tear down
        """
        self.driver.close()
