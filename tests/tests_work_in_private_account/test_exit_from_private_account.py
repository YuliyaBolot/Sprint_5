from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Личный кабинет» и кликнуть по ней
private_office_buttons = driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
private_office_buttons.click()

# Ввести почту и пароль
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

registration_fields[0].send_keys("YuliyaBolotskikh4992@yandex.ru")
registration_fields[1].send_keys("Kotya1")

# Найти кнопку «Войти» и кликнуть по ней
enter_button = driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button[text() = 'Войти']")
enter_button.click()

# Дождаться загрузки главной страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "main")))

# Снова зайти в «Личный кабинет»
private_office_buttons = driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']").click()

# Дождаться загрузки страницы личного кабинета
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_account__vgk_w")))

# Найти кнопку «Выход» и кликнуть по ней
exit_button = driver.find_element(By.XPATH, ".//ul[@class = 'Account_list__3KQQf mb-20']//button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
exit_button.click()

# Дождаться загрузки страницы для входа в личный кабинет
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

driver.quit()
