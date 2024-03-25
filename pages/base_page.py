from selenium.common.exceptions import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException
)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from math import log, sin


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Method related specifically to check tests are written on Selenium
    # for automation course
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        
    def open(self):
        self.browser.get(self.url)
        
    # Verification methods
    
    def is_element_present(self, locator: tuple):
        try:
            self.browser.find_element(*locator)
        except (NoSuchElementException):
            return False
        
        return True
    
    def is_not_element_present(self, locator: tuple, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
                )
        except TimeoutException:
            return True

        return False
    
    def is_element_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(
                self.browser, timeout, 1, TimeoutException).until_not(
                    EC.presence_of_element_located(locator)
                    )
        except TimeoutException:
            return False

        return True
    
    def verify_elements_text_match(self, locator_compared, locator_main):
        try:
            element_compared = self.browser.find_element(*locator_compared)
            element_main = self.browser.find_element(*locator_main)
            assert element_compared.text == element_main.text
        except (NoSuchElementException):
            return False, "One of elements is not found"
        except (AssertionError):
            return False, f"Elements text doesn't match: {element_compared.text} != {element_main.text}"
        
        return True, (element_compared.text, element_main.text)
