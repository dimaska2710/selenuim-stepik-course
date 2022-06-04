import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegForms(unittest.TestCase):

    browser = None
    reg1_link = "http://suninjuly.github.io/registration1.html"
    reg2_link = "http://suninjuly.github.io/registration2.html"
    welcome_txt = "Congratulations! You have successfully registered!"

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def test_reg1(self):
        self.browser.get(self.reg1_link)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("mail@mail.ru")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(self.welcome_txt, welcome_text,
                         f"Welcome text '{welcome_text}' is not equal to expected")

    def test_reg2(self):
        self.browser.get(self.reg2_link)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("mail@mail.ru")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(self.welcome_txt, welcome_text,
                         f"Welcome text '{welcome_text}' is not equal to expected")

    def tearDown(self) -> None:
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
