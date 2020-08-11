from constants import (
    documentation_link, breeds_list_link, about_link, submit_your_dog, vertical_nav, docs_url, breeds_list_url,
    about_url, submit_your_dog_url, email_input_field, test_email, subscribe_button, subscription_error
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

    def test_email_already_subscribed(self):
        """
        Verifies that already subscribed email displays error
        """
        self.page.subscribe_with_email(email_input_field, test_email, subscribe_button)
        self.page.move_driver_to_tab(1)
        self.assertTrue(
            f"{test_email} is already subscribed to list Website" or
            f"Recipient {test_email} has too many recent signup requests" in
            self.page.get_element_text(subscription_error),
            "Already subscribed error message not found!"
        )
