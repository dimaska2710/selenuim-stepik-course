import time

from selenium.webdriver.common.by import By


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(url)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed(), \
        "The 'add to cart' button is not available"

    # be welcome to check my solution!
    time.sleep(3)

