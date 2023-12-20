from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Начинки» и кликнуть по ней
fillings = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Начинки']")
fillings.click()

# Прокрутить страницу до начинок
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")
driver.execute_script("arguments[0].scrollIntoView();", burger_ingredients[2])

driver.quit()
