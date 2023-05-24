from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
  return str(int(x)+int(y))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = calc(x,y)
    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"option[value='{z}']").click()
    # или:
    # dropdown = Select(browser.find_element(By.ID, "dropdown"))
    # dropdown.select_by_value(z)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
