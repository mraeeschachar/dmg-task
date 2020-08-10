import requests
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    page_url = None

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_page(self):
        """
        Checks if the browser is on the correct page
        """
        self.wait_for_ajax()
        assert self.page_url in self.driver.current_url

    def wait_for_ajax(self):
        """
        Wait for jQuery to be loaded and for all ajax requests to finish
        """
        return self.driver.execute_script(
            "return typeof(jQuery)!='undefined' && jQuery.active==0")

    def wait_for_visibility(self, wait_element):
        """
        Wait for visibility of element
        """
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, wait_element)),
            message=f"Visibility timeout {wait_element}"
        )

    def find_css(self, element):
        """
        Find element css as provided in element
        """
        self.wait_for_visibility(element)
        return self.driver.find_element_by_css_selector(element)

    def find_css_list(self, element_list):
        """
        Find element css list as provided in element
        """
        return self.driver.find_elements_by_css_selector(element_list)

    @staticmethod
    def verify_href_link_status_code(element):
        """
        Checks if the element has a href link and verifies that the status
        code response is 200
        """
        element_href = element.get_attribute("href")
        element_href_response = requests.get(element_href)
        if not element_href_response.status_code == 200:
            return False
        return True

    @staticmethod
    def verify_image_source_status_code(element):
        """
        Checks if element has images sources and verifies that the status
        code response is 200
        """
        image = element.find_element_by_tag_name("img")
        image_src = image.get_attribute("src")
        image_src_response = requests.get(image_src)
        if not image_src_response.status_code == 200:
            return False
        return True
