from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject


class PageHeader:
    def __init__(self):
        pass

    LOGO = UiObject(By.XPATH, '//*[@id="__next"]/header/div[1]/div/img')
    OUR_COMPANY = UiObject(By.XPATH, '//*[@id="__next"]/header/nav/a[1]')
    LOCATIONS = UiObject(By.XPATH, '//*[@id="__next"]/header/nav/a[2]')
    CONTACT = UiObject(By.XPATH, '//*[@id="__next"]/header/nav/a[3]')

    @staticmethod
    def click_logo(self):
        PageHeader.LOGO.click()
        from ui_test.pages.homepage.HomePage import HomePage
        return HomePage()

    @staticmethod
    def click_our_company(self):
        PageHeader.OUR_COMPANY.click()
        from ui_test.pages.our_company.OurCompany import OurCompany
        return OurCompany()

    @staticmethod
    def click_locations(self):
        PageHeader.LOCATIONS.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()

    @staticmethod
    def click_contact(self):
        PageHeader.CONTACT.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()
