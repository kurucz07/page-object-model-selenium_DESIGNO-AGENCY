from selenium.webdriver.common.by import By
from ui_test.UiObjects import UiObject


class PageFooter:
    def __init__(self):
        pass

    LOGO = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div/div/img')
    OUR_COMPANY = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/nav/a[1]')
    LOCATIONS = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/nav/a[2]')
    CONTACT = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/nav/a[3]')
    FACEBOOK = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[2]/div[3]/a[1]/div/img')
    YOUTUBE = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[2]/div[3]/a[2]/div/img')
    PINTEREST = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[2]/div[3]/a[4]/div/img')
    INSTAGRAM = UiObject(By.XPATH, '//*[@id="__next"]/footer/div/div[2]/div[3]/a[5]/div/img')

    @staticmethod
    def click_logo(self):
        PageFooter.LOGO.click()
        from ui_test.pages.homepage.HomePage import HomePage
        return HomePage()

    @staticmethod
    def click_our_company(self):
        PageFooter.OUR_COMPANY.click()
        from ui_test.pages.our_company.OurCompany import OurCompany
        return OurCompany()

    @staticmethod
    def click_locations(self):
        PageFooter.LOCATIONS.click()
        from ui_test.pages.locations.Locations import Locations
        return Locations()


    @staticmethod
    def click_contact(self):
        PageFooter.CONTACT.click()
        from ui_test.pages.contact.Contact import Contact
        return Contact()


