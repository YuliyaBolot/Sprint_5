import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Личный кабинет» и кликнуть по ней
private_office_buttons = driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
private_office_buttons.click()

# Найти ссылку "Зарегистрироваться" и кликнуть по ней
registration_link = driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj")
registration_link.click()

# Ввести данные для регистрации
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

new_login = f"YuliaBolotskikh4{random.randint(100, 999)}@yandex.ru"

new_password = f"{random.randint(100000, 1000000)}"

registration_fields[0].send_keys("Юлия")
registration_fields[1].send_keys(new_login)
registration_fields[2].send_keys(new_password)

# Найти кнопку "Зарегистрироваться" и кликнуть по ней
registration_button = driver.find_element(By.XPATH, ".//form//button[text()='Зарегистрироваться']")
registration_button.click()

# Добавить явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))

driver.quit()

