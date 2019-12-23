from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Задаем время  "задержки поиска" так же производим поиск до появления нужного нам текста "$100"
    book = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    bt_book = browser.find_element(By.ID, "book")
    bt_book.click()
    
    # Решение функции
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # Находим кнопку "Подтвердить"
    sub_bt = browser.find_element(By.ID, "solve")
    sub_bt.click()

finally:
    time.sleep(5)
    browser.quit()