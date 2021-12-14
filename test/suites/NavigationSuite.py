from test_junkie.decorators import test, Suite
from ui_test.pages.our_company.OurCompany import OurCompany
from ui_test.pages.locations.Locations import Locations
from ui_test.pages.contact.Contact import Contact
from ui_test.pages.homepage.HomePage import HomePage
from test.TestRules import TestRules


@Suite(parameters=[HomePage,Contact, Locations, OurCompany], rules=TestRules)
class NavigationSuite:

    @staticmethod
    def __validate_page_properties(page):
        """
        There are common validation steps in this suite,
        thus it was unified under this method.
        This method validates:
        - expected and actual page URL
        - expected and actual page Title
        Based on the Page Object definitions
        :param page: Object, any page object
        :return: None
        """
        expected_url, actual_url = page.expected_url, page.get_actual_url()
        assert expected_url in actual_url, \
            "Expected URL: {} Actual URL: {}".format(expected_url, actual_url)
        expected_title, actual_title = page.expected_title, page.get_actual_title()
        assert expected_title in actual_title, \
            "Expected Title: {} Actual Title: {}".format(expected_title, actual_title)

    @test(parameters=["about", "locations", "contact"],
          parallelized_parameters=True)
    def verify_header_navigation(self, suite_parameter, parameter):
        page = suite_parameter().open()
        page = getattr(page.header, f"click_{parameter}")()
        NavigationSuite.__validate_page_properties(page)

    @test(parameters=["about", "locations", "contact"],
          parallelized_parameters=True)
    def verify_footer_navigation(self, suite_parameter, parameter):
        page = suite_parameter().open()
        page = getattr(page.footer, f"click_{parameter}")()
        NavigationSuite.__validate_page_properties(page)