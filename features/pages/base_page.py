from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    def __init__(self, browser, base_url='https://material.angular.io/components/categories'):
        self.base_url = base_url
        self.browser = browser

    def find_element(self, selector, value):
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((selector, value))
        )
        return self.browser.find_element(selector, value)
