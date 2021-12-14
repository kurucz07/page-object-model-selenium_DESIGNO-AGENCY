from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject
from ui_test.BasePage import BasePage
from ui_test.pages.components.PageHeader import PageHeader
from ui_test.pages.components.Pagefooter import PageFooter
from ui_test.utils.Settings import Settings


class WebDesign(BasePage, PageFooter, PageHeader):

    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Web Design - We Design Web Applications",
                          directory="/portfolios/web-design")
        self.header = PageHeader
        self.footer = PageFooter

    GET_IN_TOUCH = UiObject(By.XPATH, '//*[@id="__next"]/div/div/section[3]/div/div[2]/button')
    APP_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div[1]/div')
    GRAPHIC_DESIGN = UiObject(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div[2]/div')

    def click_get_in_touch(self):
        WebDesign.GET_IN_TOUCH.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()

    def click_app_design(self):
        WebDesign.APP_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.AppDesign import AppDesign
        return AppDesign()

    def click_graphic_design(self):
        WebDesign.GRAPHIC_DESIGN.click()
        from ui_test.pages.homepage.homepage_components.GraphicDesign import GraphicDesign
        return GraphicDesign()