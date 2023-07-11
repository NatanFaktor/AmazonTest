from selenium import webdriver
from selenium.webdriver.common.by import By


class Mice_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def item_num(self, num: int):
        item_list = self.driver.find_elements(By.CSS_SELECTOR, "[class='a-link-normal s-underline-text s-underline-link"
                                                               "-text s-link-style a-text-normal']")
        print(item_list[num].text)
        item_list[num].click()

