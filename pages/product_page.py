from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_item_to_basket(self):
        login_link = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()
        
    def should_be_item_is_added_message(self):
        assert self.is_element_present(ProductPageLocators.ADD_SUCCESS_MESSAGE), "Add item success message is missing"
        
    def should_be_added_item_name_in_success_message(self):
        verif_result, message = self.verify_elements_text_match(
            ProductPageLocators.ITEM_NAME_PRODUCT_MAIN,
            ProductPageLocators.ITEM_NAME_ADD_SUCCESS_MESSAGE
            )
        assert verif_result, message
    
    def should_be_total_cost_message(self):
        assert self.is_element_present(ProductPageLocators.TOTAL_COST_MESSAGE), "Total cost message is missing"
        
    def should_be_added_item_price_in_total_message(self):
        verif_result, message = self.verify_elements_text_match(
            ProductPageLocators.ITEM_PRICE_PRODUCT_MAIN,
            ProductPageLocators.TOTAL_COST_TOTAL_COST_MESSAGE
            )
        assert verif_result, message
