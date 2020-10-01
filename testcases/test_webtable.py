from selenium import webdriver
import unittest
from testdata.webtable_testdata import WebTableData
from pages.WebTablePage import WebTable, HomePage
from locators.webtable_locator import HomePageLocator


class WebTableHandle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(WebTableData.CHROME_EXECUTABLE_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(WebTableData.BASE_URL)

    def test_validate_webtable(self):
        homepage = HomePage(self.driver)
        homepage.scroll_down()
        homepage.add_product(HomePageLocator.product_img1, HomePageLocator.add_to_cart1)
        homepage.continue_shopping()
        homepage.add_product(HomePageLocator.product_img2, HomePageLocator.add_to_cart2)
        homepage.continue_shopping()
        homepage.add_product(HomePageLocator.product_img3, HomePageLocator.add_to_cart3)
        homepage.proceed_to_checkout()

        webtable = WebTable(self.driver)
        webtable.get_column_count()
        webtable.get_row_count()
        webtable.print_table_contents()

    def tearDown(self):
        self.driver.close()
