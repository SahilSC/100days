from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(url)
min = 5
sec_update = 5
timeout = time.time() + min*60
types = ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine','buyShipment','buyAlchemy lab', 'buyPortal','buyTime machine']
len = len(types)
while time.time() < timeout:
    temptimeout = time.time() + sec_update
    while True:
        driver.find_element(By.ID, "cookie").click()
        if time.time() > temptimeout:
            break
    curcookies = int(driver.find_element(By.ID, "money").text)
    for num in range(len-1, -1, -1):
        while driver.find_element(By.ID, types[num]).get_attribute("class")=='':
            driver.find_element(By.ID, types[num]).click()
            time.sleep(.2)


driver.quit()