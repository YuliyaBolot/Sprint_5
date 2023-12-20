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
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

# Ввести данные для регистрации
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

registration_fields[0].send_keys("Юлия")
registration_fields[1].send_keys("YuliyaBolotskikh4992@yandex.ru")

# Ввести пароль меньше 6 символов
try:
    registration_fields[2].send_keys("Kotya")
    registration_button = driver.find_element(By.XPATH, ".//form//button[text()='Зарегистрироваться']")
    registration_button.click()
    raise Exception('Некорректный пароль. Минимальный пароль — шесть символов.')
except Exception as e:
    print(e)

driver.quit()
