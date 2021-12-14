from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject
from ui_test.BasePage import BasePage
from ui_test.pages.components.PageHeader import PageHeader
from ui_test.pages.components.Pagefooter import PageFooter
from ui_test.utils.Settings import Settings


class OurCompany(BasePage, PageFooter, PageHeader):

    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="About - We Are More Than a Brand",
                          directory="/about")
        self.header = PageHeader
        self.footer = PageFooter

    GET_IN_TOUCH = UiObject(By.XPATH, '//*[@id="__next"]/div/div/div[3]/div/div[2]/button')
    CANADA = UiObject(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[1]/button')
    AUSTRALIA = UiObject(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]/button')
    UNITED_KINGDOM = UiObject(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[3]/button')

    def click_get_in_touch(self):
        OurCompany.GET_IN_TOUCH.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()

    def click_canada(self):
        OurCompany.CANADA.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()

    def click_australia(self):
        OurCompany.AUSTRALIA.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()

    def click_united_kingdom(self):
        OurCompany.UNITED_KINGDOM.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()