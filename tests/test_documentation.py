from constants import (list_all_breeds, random_image, browse_breed_list,
                       by_sub_breed, by_breed, end_point_list
                       )
from pages.documentation_page import DocumentationPage
from tests.test_base import TestBase


class TestDocumentation(TestBase):
    """
    Home page tests
    """
    PageClass = DocumentationPage

    def test_endpoint_list(self):
        """
        Verify that all expected end point list elements are available
        """
        option_list = [
            list_all_breeds, random_image, by_breed, by_sub_breed,
            browse_breed_list
        ]
        self.assertTrue(
            self.page.verify_end_point_options(end_point_list, option_list),
            "All expected end point items not found!")
