from selenium import webdriver
from selenium.webdriver.common.by import By


class Item_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def show_price(self):
        first_price_option = self.driver.find_elements(By.CSS_SELECTOR,
                                                       "[id='corePrice_feature_div']>div>div>span>span")
        second_price_option = self.driver.find_elements(By.CSS_SELECTOR,
                                                        "[id='corePrice_feature_div']>div>span>span")

        if first_price_option:
            print(first_price_option[1].text)
        else:
            print(second_price_option[1].text)
