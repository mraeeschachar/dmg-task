from constants import (
    documentation_link, breeds_list_link, about_link, submit_your_dog, vertical_nav, docs_url, breeds_list_url,
    about_url, submit_your_dog_url
)
from pages.home_page import HomePage
from tests.test_base import TestBase


class TestHome(TestBase):
    """
    Home page tests
    """
    PageClass = HomePage

    def test_main_links(self):
        """
        Verify that main links are working
        """
        self.assertTrue(self.page.verify_links_status_code(vertical_nav),
                        "Incorrect status code of main links!")

    def test_side_navigation(self):
        """
        Verifies that side navigation is working
        """
        side_nav = [
            documentation_link, breeds_list_link, about_link, submit_your_dog
        ]
        verification_urls = [
            docs_url, breeds_list_url, about_url, submit_your_dog_url
        ]
        for link, verification in zip(side_nav, verification_urls):
            self.page.click_link_on_home_page(link)
            self.assertTrue(verification in self.driver.current_url)
