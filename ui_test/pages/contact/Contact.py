from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject
from ui_test.BasePage import BasePage
from ui_test.pages.components.PageHeader import PageHeader
from ui_test.pages.components.Pagefooter import PageFooter
from ui_test.utils.Settings import Settings


class Contact(BasePage, PageFooter, PageHeader):

    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Contact - We Want to Hear From You",
                          directory="/contact")
        self.header = PageHeader
        self.footer = PageFooter

    CANADA = UiObject(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div[1]/button')
    AUSTRALIA= UiObject(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div[2]/button')
    UNITED_KINGDOM= UiObject(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div[3]/button')

    def click_canada(self):
        Contact.CANADA.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()

    def click_australia(self):
        Contact.AUSTRALIA.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()

    def click_united_kingdom(self):
        Contact.UNITED_KINGDOM.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()