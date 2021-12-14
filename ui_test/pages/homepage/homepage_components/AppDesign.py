from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject
from ui_test.BasePage import BasePage
from ui_test.pages.components.PageHeader import PageHeader
from ui_test.pages.components.Pagefooter import PageFooter
from ui_test.utils.Settings import Settings


class AppDesign(BasePage, PageFooter, PageHeader):

    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="App Design - We Design Mobile Applications",
                          directory="/portfolios/app-design")
        self.header = PageHeader
        self.footer = PageFooter

    GET_IN_TOUCH = UiObject(By.XPATH, '//*[@id="__next"]/div/div/section[3]/div/div[2]/button')
    WEB_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div[1]/div')
    GRAPHIC_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div[2]/div')

    def click_get_in_touch(self):
        AppDesign.GET_IN_TOUCH.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()

    def click_web_design(self):
        AppDesign.WEB_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.WebDesign import WebDesign
        return WebDesign()

    def click_graphic_design(self):
        AppDesign.GRAPHIC_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.GraphicDesign import GraphicDesign
        return GraphicDesign()