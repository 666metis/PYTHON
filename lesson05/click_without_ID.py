from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Откроем страницу 

driver.get("http://uitestingplayground.com/dynamicid")

sleep(1)
# Кликнем на синюю кнопку

blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()

sleep(1)

