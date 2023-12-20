from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Войти в аккаунт» и кликнуть по ней
login_to_account_button = driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button[text() = 'Войти в аккаунт']")
login_to_account_button.click()

# Ввести почту и пароль
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

registration_fields[0].send_keys("YuliyaBolotskikh4992@yandex.ru")
registration_fields[1].send_keys("Kotya1")

# Найти кнопку «Войти» и кликнуть по ней
enter_button = driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
enter_button.click()

# Дождаться загрузки главной страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "main")))

driver.quit()
