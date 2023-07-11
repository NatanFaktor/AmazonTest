from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Main_Page:
    computer_mice_button = None

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def computer_mice_exist(self):
        try:
            self.computer_mice_button = self.driver.find_element(By.CSS_SELECTOR,
                                                                 "[aria-label='Computer mice']")
            return True
        except NoSuchElementException:
            return False

    def computer_mice(self):
        if self.computer_mice_exist():
            return self.computer_mice_button

    def click_computer_mice(self):
        self.computer_mice().click()

    