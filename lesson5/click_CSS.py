from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Откроем страницу 

driver.get("http://uitestingplayground.com/classattr")

sleep(1)

# Кликнем на синюю кнопку
blue_btn = ("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button = driver.find_element(By.XPATH, blue_btn)

blue_button.click()