from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initializing the chrome driver
driver = webdriver.Chrome()

# test scenario starts here
driver.get("http://automationpractice.com")
time.sleep(5)

search_box = driver.find_element(By.NAME, 'search_query')
#search_box = driver.find_element(By.PATH, 'search_query')
#search_box = driver.find_element(By.CSS_SELECTOR, 'search_query')
search_box.send_keys("dress")

time.sleep(5)

driver.close()
