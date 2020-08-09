from pages.base_page import BasePage


class DocumentationPage(BasePage):

    page_url = "https://dog.ceo/dog-api/documentation/"

    def verify_end_point_options(self, element, endpoint_list):
        """
        Verifies end point option list
        """
        endpoints = self.find_css(element)
        for text in endpoint_list:
            if text not in endpoints.text:
                return False
        return True
