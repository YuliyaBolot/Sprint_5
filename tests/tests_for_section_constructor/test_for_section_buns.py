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

# Найти кнопку «Булки» и кликнуть по ней
buns = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']/div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
buns.click()

# Прокрутить страницу до булок
burger_ingredients = driver.find_elements(By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT']")
driver.execute_script("arguments[0].scrollIntoView();", burger_ingredients[0])

driver.quit()
