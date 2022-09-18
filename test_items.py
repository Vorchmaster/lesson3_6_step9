from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_buy_button_exists(browser):
    browser.get(link)
    btn = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(btn) != 0, "No buy button."
    time.sleep(5)
