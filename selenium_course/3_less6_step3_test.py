import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize(
    'url', (
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    )
)
def test_feedback(browser, answer, url):
    browser.get(url)
    WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "string-quiz__textarea"))).send_keys(answer)
    WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    try:
        WebDriverWait(browser, 5).until(
            expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!"))
    except TimeoutException:
        print(browser.find_element(By.CLASS_NAME, "smart-hints__hint").text)
