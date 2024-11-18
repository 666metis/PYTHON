from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Откроем страницу 

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


# Кликнем 5 раз на кнопку "Add Ellement"

btn = ("button")
for i in range(5):
    add_btn = driver.find_element(By.CSS_SELECTOR, btn)
    add_btn.click()

sleep(5)

# Список кнопок "Delete"

delete_btn = ("button.added-manually")
delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_btn)

# Выведем размер списка

print(len(delete_buttons))