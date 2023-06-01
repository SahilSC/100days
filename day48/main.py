from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://docs.google.com/forms/d/e/1FAIpQLSfWz6svdZmTThEiaq0lQRe0v85MNJx8vBB5jq5Ajd8DJ-0rEw/viewform"
driver = webdriver.Chrome()

driver.get(url)
name = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd')
name.send_keys("rushil")

say_whatever = driver.find_element(By.CSS_SELECTOR, 'textarea')
say_whatever.send_keys("im gay")

enter = driver.find_element(By.CSS_SELECTOR, 'span.l4V7wb.Fxmcue')
enter.click()
time.sleep(5)
driver.quit()