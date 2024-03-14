from .pages.product_page import ProductPage
from time import sleep

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_is_added_message()
    page.should_be_added_item_name_in_success_message()
    page.should_be_total_cost_message()
    page.should_be_added_item_price_in_total_message()