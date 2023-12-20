from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site')

# Найти кнопку «Соусы» и кликнуть по ней
sauces = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']//span[text() = 'Соусы']")
sauces.click()

# Прокрутить страницу до соусов
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")
driver.execute_script("arguments[0].scrollIntoView();", burger_ingredients[1])

driver.quit()

