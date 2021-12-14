from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject
from ui_test.BasePage import BasePage
from ui_test.pages.components.PageHeader import PageHeader
from ui_test.pages.components.Pagefooter import PageFooter
from ui_test.utils.Settings import Settings


class HomePage(BasePage, PageFooter, PageHeader):

    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Designo - Software Development Agency",
                          directory="")
        self.header = PageHeader
        self.footer = PageFooter

    GET_IN_TOUCH = UiObject(By.XPATH, '//*[@id="__next"]/div/div[2]/section[2]/div/div[2]/button')
    LEARN_MORE = UiObject(By.XPATH, '//*[@id="__next"]/div/div[1]/section/div[1]/button')
    WEB_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div[1]/div/section/div[1]/div')
    APP_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div[1]/div/section/div[2]/div')
    GRAPHIC_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div[1]/div/section/div[3]/div')

    def click_get_in_touch(self):
        HomePage.GET_IN_TOUCH.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()

    def click_learn_more(self):
        HomePage.LEARN_MORE.click()
        from ui_test.pages.our_company.OurCompany import OurCompany
        return OurCompany()

    def click_web_design(self):
        HomePage.WEB_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.WebDesign import WebDesign
        return WebDesign()

    def click_app_design(self):
        HomePage.APP_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.AppDesign import AppDesign
        return AppDesign()

    def click_graphic_design(self):
        HomePage.GRAPHIC_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.GraphicDesign import GraphicDesign
        return GraphicDesign()
