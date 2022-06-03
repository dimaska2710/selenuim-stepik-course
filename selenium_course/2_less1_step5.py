import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    robo = browser.find_element(By.ID, "robotCheckbox")
    robo.click()
    robo_rule = browser.find_element(By.ID, "robotsRule")
    robo_rule.click()
    time.sleep(1)
    btn = browser.find_element(By.CLASS_NAME, "btn-default")
    btn.click()
finally:
    time.sleep(10)
    browser.quit()


