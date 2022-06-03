import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    robo = browser.find_element(By.ID, "robotCheckbox")
    robo.click()
    robo_rule = browser.find_element(By.ID, "robotsRule")
    robo_rule.click()
    btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    btn.click()
finally:
    time.sleep(10)
    browser.quit()


