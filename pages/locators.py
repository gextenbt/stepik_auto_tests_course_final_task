from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    ADD_SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')
    TOTAL_COST_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]')
    ITEM_NAME_ADD_SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    TOTAL_COST_TOTAL_COST_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]//strong')

    ITEM_NAME_PRODUCT_MAIN = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    ITEM_PRICE_PRODUCT_MAIN = (By.CSS_SELECTOR, 'p.price_color ')
    

