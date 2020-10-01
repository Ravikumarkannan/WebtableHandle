from selenium.webdriver.common.by import By


class WebTableLocator(object):
    table_column = (By.XPATH, "//table[@id='cart_summary']//thead/tr/th")
    table_row = (By.XPATH, "//table[@id='cart_summary']//tbody/tr")
    table_content = (By.XPATH, "//table[@id='cart_summary']//tbody/tr/td")
    table_footer = (By.XPATH, "//table[@id='cart_summary']/tfoot/tr/td")


class HomePageLocator(object):
    scroll = (By.XPATH, "//a[text()='Popular']")

    product_img1 = (By.XPATH, "(//div[@class='product-image-container']/a/img)[1]")
    product_img2 = (By.XPATH, "(//div[@class='product-image-container']/a/img)[2]")
    product_img3 = (By.XPATH, "(//div[@class='product-image-container']/a/img)[3]")

    add_to_cart1 = (By.XPATH, "(//span[text()='Add to cart'])[1]")
    add_to_cart2 = (By.XPATH, "(//span[text()='Add to cart'])[2]")
    add_to_cart3 = (By.XPATH, "(//span[text()='Add to cart'])[3]")

    close_window = (By.XPATH, "//span[@title='Close window']")
    continue_shopping = (By.XPATH, "//span[@title='Continue shopping']")
    proceed_to_checkout = (By.XPATH, "//span[contains(text(),'Proceed')]")
