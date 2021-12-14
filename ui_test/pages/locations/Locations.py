from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject
from ui_test.BasePage import BasePage
from ui_test.pages.components.PageHeader import PageHeader
from ui_test.pages.components.Pagefooter import PageFooter
from ui_test.utils.Settings import Settings


class Locations(BasePage, PageFooter, PageHeader):

    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Locations - Find Our Closest Offices",
                          directory="/locations")
        self.header = PageHeader
        self.footer = PageFooter

    CANADA = UiObject(By.XPATH, '//*[@id="mapDiv"]/div/div/div[4]/div/div/div/div/div[2]/a')
    AUSTRALIA = UiObject(By.XPATH, '//*[@id="mapDiv"]/div/div/div[4]/div/div/div/div/div[2]/a')
    UNITED_KINGDOM = UiObject(By.XPATH, '//*[@id="mapDiv"]/div/div/div[4]/div/div/div/div/div[2]/a')
    GET_IN_TOUCH =UiObject(By.XPATH, '//*[@id="__next"]/div/section/div/div[2]/button')

    def click_canada(self):
        Locations.CANADA.click()
        from ui_test.BasePage import BasePage
        return BasePage(domain='https://www.google.com/maps/place/', title= 'Wellington St W - Google Maps',
                        directory='Wellington+St+W,+Toronto,+ON,+Canada/@43.644016,'
                                  '-79.394539,16z/data=!4m5!3m4!1s0x882b34d9a0737d9f:0xbc1ae74f23fabf4e!8m2!3d43.6440163!4d-79.'
                                  '3945394?hl=en')

    def click_australia(self):
        Locations.AUSTRALIA.click()
        from ui_test.BasePage import BasePage
        return BasePage(domain='https://www.google.com/maps/place/', title='19 Balonne St - Google Maps',
                        directory='19+Balonne+St,+Narrabri+NSW+2390,'
                               '+Australia/@-30.329398,149.78824,16z/data=!4m5!3m4!1s0x6ba73450a680702d:'
                                  '0x44a309bd6607346e!8m2!3d-30.'
                               '3293985!4d149.7882399?hl=en')

    def click_united_kingdom(self):
        Locations.UNITED_KINGDOM.click()
        from ui_test.BasePage import BasePage
        return BasePage(domain='https://www.google.com/maps/place/', title='13 Colorado Cl - Google Maps',
                        directory='13+Colorado+Cl,+Dover+CT16+2AY,+UK/@51.141626,1.298017,16z/data='
                                  '!4m5!3m4!1s0x47debac4c634012f:0xdfbca00b6f6c3a36!8m2!3d51.1416261!4d1.2980168?hl=en')

    def click_get_in_touch(self):
        Locations.GET_IN_TOUCH.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()
