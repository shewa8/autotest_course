import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Проверяем значение атрибута checked у people_radio:
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # Проверяем значение атрибута checked у robot_radio:
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None

    # Проверяем значение атрибута disabled у Submit:
    sub_btn = browser.find_element_by_class_name("btn")
    sub_btn_checked = sub_btn.get_attribute("disabled")
    print("value of Submit btn: ", sub_btn_checked)
    assert sub_btn_checked is None

    # Проверяем значение атрибута disabled у Submit после тайм-аута:
    time.sleep(10)
    sub_btn.get_attribute("disabled")
    sub_btn_checked = sub_btn.get_attribute("disabled")
    print("value of Submit btn after timer: ", sub_btn_checked)
    assert sub_btn_checked is not None

finally:
    browser.quit()



