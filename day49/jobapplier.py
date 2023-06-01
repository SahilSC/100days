from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3619158604&f_AL=true&f_E=2&f_SB2=4&f_TPR=r2592000&f_WT=2&keywords=python%20developer&refresh=true'
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys("icycoldchill101@gmail.com")
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys(os.environ['PASSWORD'])
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()

elements = driver.find_elements(By.CSS_SELECTOR, 'div.jobs-search-results-list ul.scaffold-layout__list-container li.jobs-search-results__list-item')
print(len(elements))
time.sleep(10)


for ele in elements:
    ele.click()
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    save_element = driver.find_element(By.CSS_SELECTOR,"button.jobs-save-button")
    save_element.click()


# save_element = driver.find_element(By.CSS_SELECTOR,"button[data-tracking-control-name='public_jobs_topcard-save-job'")
# save_element.click()



# input = driver.find_element(By.NAME, 'email-input-page__input')
# input.send_keys("icycoldchill101@gmail.com")
# continue_button = driver.find_element(By.CSS_SELECTOR, '[data-tracking-control-name="public_jobs_save-job-form-continue"]')
# continue_button.click()
#
# pass_input = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/div[2]/div/form/div[1]/div[2]/div/div/input')
# pass_input.send_keys(os.environ['PASSWORD'])
# time.sleep(3)
#
# sign_in = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/section/div/div[2]/div/form/div[2]/button')
# sign_in.click()
# time.sleep(15)
#
