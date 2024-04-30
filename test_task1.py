
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_search_Firefox_br():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('https://google.com/')
    consent = browser.find_element(By.ID, 'W0wltc')
    consent.click()
    search_field = browser.find_element(By.ID, 'APjFqb')
    search_field.clear()
    search_field.send_keys('samsung galaxy')
    search_field.send_keys(Keys.RETURN)
    time.sleep(7)

    elems = browser.find_elements(By.CSS_SELECTOR, "div#search div.yuRUbf a")
    elems[10].click()
    time.sleep(5)
    browser.close()

def test_search_Chorme_br():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://google.com/')
    consent = browser.find_element(By.ID, 'W0wltc')
    consent.click()
    search_field = browser.find_element(By.ID, 'APjFqb')
    search_field.clear()
    search_field.send_keys('samsung galaxy')
    search_field.send_keys(Keys.RETURN)
    time.sleep(7)

    elems = browser.find_elements(By.CSS_SELECTOR, "div#search div.yuRUbf a")
    elems[10].click()
    time.sleep(5)
    browser.close()