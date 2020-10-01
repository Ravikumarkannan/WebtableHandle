from selenium import webdriver
from locators.webtable_locator import WebTableLocator, HomePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).text

    def mouse_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()


class HomePage(BasePage):

    def scroll_down(self):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(HomePageLocator.scroll))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def add_product(self, product, add_to_cart):
        self.mouse_hover(product)
        self.click(add_to_cart)

    def continue_shopping(self):
        self.click(HomePageLocator.continue_shopping)

    def proceed_to_checkout(self):
        self.click(HomePageLocator.proceed_to_checkout)


class WebTable(BasePage):

    def get_row_count(self):
        row_number = len(self.driver.find_elements(*WebTableLocator.table_row))
        print(f"Number of rows in table : {row_number}")

    def get_column_count(self):
        column_number = len(self.driver.find_elements(*WebTableLocator.table_column))
        print(f"Number of columns in table : {column_number}")

    def print_table_contents(self):
        elements = self.driver.find_elements(*WebTableLocator.table_content)
        elements_foot = self.driver.find_elements(*WebTableLocator.table_footer)

        for index in range(len(elements)):
            print(elements[index].text)

        for index in range(len(elements_foot)):
            print(elements_foot[index].text)
