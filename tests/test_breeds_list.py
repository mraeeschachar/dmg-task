from constants import (dog_selector, boxer_breed, dog_image, fetch_dog_button
                       )
from pages.breeds_list_page import BreedsListPage
from tests.test_base import TestBase


class TestBreedsList(TestBase):
    """
    Home page tests
    """
    PageClass = BreedsListPage

    def test_boxer_breed(self):
        """
        Verify that boxer breed can be fetched and image displays
        """
        self.page.select_breed(dog_selector, boxer_breed, fetch_dog_button)
        self.assertTrue(self.page.verify_images_status_code(dog_image))
