from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
        )
        self.browser.get(self.base_url)

    def clickMenu(self,menuItem):
        self.find_element(By.CSS_SELECTOR, "[aria-label='" + menuItem + "']").click()

    def clickSubMenu(self,menuItem):
        self.find_element(By.CSS_SELECTOR, "[href='/components/" + menuItem + "']").click()