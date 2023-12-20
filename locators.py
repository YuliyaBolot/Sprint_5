from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Кнопка входа в «Личный кабинет»
private_office_buttons = driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")

# Поля ввода для регистрации
registration_fields = driver.find_elements(By.XPATH, ".//fieldset[@class = 'Auth_fieldset__1QzWN mb-6']//input[@class = 'text input__textfield text_type_main-default']")

# Ссылка «Зарегистрироваться»
registration_link = driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj")

# Кнопка «Зарегистрироваться»
registration_button = driver.find_element(By.XPATH, ".//form//button[text()='Зарегистрироваться']")

# Кнопка «Войти в аккаунт»
login_to_account_button = driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button[text() = 'Войти в аккаунт']")

# Кнопка «Войти» для входа в аккаунт
enter_button = driver.find_element(By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

# Кнопка «Выйти» из аккаунта
exit_button = driver.find_element(By.XPATH, ".//ul[@class = 'Account_list__3KQQf mb-20']//button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']")

# Конструктор
constructor = driver.find_element(By.LINK_TEXT, "Конструктор")

# Логотип Stellar Burgers
stella_burgers = driver.find_element(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")

# Кнопка «Булки»
buns = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']/div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")

# Кнопка «Соусы» и «Начинки»
sauces = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Соусы']")

# Кнопка «Начинки»
fillings = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Начинки']")

# Списки ингредиентов для бургеров
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")