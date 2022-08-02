from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # явное ожидание 12 секунд
    wait = WebDriverWait(browser, 12)

    # ждем пока цена станет равна 100
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # нажимаем кнопку Book
    button_Boook = browser.find_element(By.CSS_SELECTOR, "#book")
    button_Boook.click()

    # находим значение выражения и заносим его в переменную
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)


    # Заполняет поле ввода, вычисленным значением
    input1 = browser.find_element(By.CSS_SELECTOR, "input[required]#answer.form-control[type='text']")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла





