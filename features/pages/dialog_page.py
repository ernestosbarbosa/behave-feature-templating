from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class DialogPage(BasePage):
    input = "[placeholder=\"What's your name?\"]";
    pickOne = "[class='mat-raised-button']";
    dialogTitle = "h1.mat-dialog-title";

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
        )

    def fillInput(self,text):
        self.find_element(By.CSS_SELECTOR, self.input).send_keys(text)

    def clickPickOne(self):
        self.find_element(By.CSS_SELECTOR, self.pickOne).click()

    def getDialogTitle(self):
        return self.find_element(By.CSS_SELECTOR, self.dialogTitle).text