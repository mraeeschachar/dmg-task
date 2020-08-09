from pages.base_page import BasePage


class BreedsListPage(BasePage):

    page_url = "https://dog.ceo/dog-api/breeds-list"

    def select_breed(self, element, breed, fetch):
        """
        Selects breed as provided in breed
        """
        selector = self.find_css(element)
        breed_selector = self.find_css(breed)
        fetch_button = self.find_css(fetch)
        selector.click()
        breed_selector.click()
        fetch_button.click()
        self.wait_for_ajax()

    def verify_images_status_code(self, element):
        """
        Finds image and verifies status code as provided in element
        """
        image_list = self.find_css_list(element)
        for img in image_list:
            if not self.verify_image_source_status_code(img):
                return False
        return True
