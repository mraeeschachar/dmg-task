from pages.base_page import BasePage


class HomePage(BasePage):

    page_url = "https://dog.ceo/dog-api/"

    def verify_links_status_code(self, element):
        """
        Verifies that provided elements href links are working as expected
        """
        selector = self.find_css(element)
        anchor = selector.find_elements_by_tag_name("a")
        for element in anchor:
            if not self.verify_href_link_status_code(element):
                return False
        return True

    def click_link_on_home_page(self, element):
        """
        Clicks link on home page as provided in element
        """
        selector = self.find_css(element)
        selector.click()
        self.wait_for_ajax()
