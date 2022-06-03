import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()


try:
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Bobby")
    browser.find_element(By.NAME, "lastname").send_keys("Brown")
    browser.find_element(By.NAME, "email").send_keys("BobbyBrown@y.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.abspath(os.path.join(current_dir, '..', 'data', '2_2_8.txt'))

    browser.find_element(By.NAME, "file").send_keys(file_path)

    browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()


