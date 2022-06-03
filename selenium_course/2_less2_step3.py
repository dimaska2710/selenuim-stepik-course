import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()


try:
    browser.get(link)

    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    su = int(a) + int(b)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(su))

    btn = browser.find_element(By.CLASS_NAME, "btn-default")
    btn.click()
finally:
    time.sleep(10)
    browser.quit()


