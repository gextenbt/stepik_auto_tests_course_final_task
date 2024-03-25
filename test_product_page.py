from pages.product_page import ProductPage
from config import ProductPageUrls
from time import sleep
import pytest 
from utils import mark_param_list


offer_promo_params = [i for i in range(10)]
xfail_offer_marks = [7]
marked_offer_params = mark_param_list(
    params=offer_promo_params,
    mark_xfail=xfail_offer_marks
    )


@pytest.mark.parametrize(
    'value', marked_offer_params
    )
def test_guest_can_add_product_to_basket_on_promo_offers(browser, value):
    link = (f"{ProductPageUrls.CATALOGUE}"
            f"coders-at-work_207/?promo=offer{value}")
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_success_message()
    page.should_be_added_item_name_in_success_message()
    page.should_be_total_cost_message()
    page.should_be_added_item_price_in_total_message()


@pytest.mark.xfail(reason="Negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = (f"{ProductPageUrls.CATALOGUE}"
            f"coders-at-work_207/")
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_add_success_message()


def test_guest_cant_see_success_message(browser):
    link = (f"{ProductPageUrls.CATALOGUE}"
            f"coders-at-work_207/")
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_not_be_add_success_message()


@pytest.mark.xfail(reason="Negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = (f"{ProductPageUrls.CATALOGUE}"
            f"coders-at-work_207/")
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_item_to_basket()
    page.should_be_add_success_message_disappeared()