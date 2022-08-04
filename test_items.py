import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button_basket) > 0, "Нет кнопки добавить товар в корзину!"

# последняя строка
