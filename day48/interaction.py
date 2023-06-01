from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
num_articles = int(driver.find_element(By.CSS_SELECTOR, "#articlecount a").text.replace(',', ''))
print(num_articles)
driver.quit()















# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# url="https://python.org"
# driver.get(url)
# dates = [tag.get_attribute(name="datetime")[:10] for tag in driver.find_elements(By.CSS_SELECTOR, 'div.event-widget ul.menu li time')]
# events = [tag.get_attribute(name="href") for tag in driver.find_elements(By.CSS_SELECTOR, 'div.event-widget ul.menu li a')]
# #
# # print(dates)
# # print(events)
# eventdict = {}
# for int in range(0, len(dates)):
#     eventdict[int] = {dates[int], events[int]}
#
# print(eventdict)
#
#







# # create webdriver object
# driver = webdriver.Chrome()
# URL = "https://www.python.org/"
# driver.get(URL)
# inputtag = driver.find_element(By.XPATH, "/html/body/div/footer/div[1]/div/ul/li[7]/ul/li[1]/a")
# print(inputtag.text)
# #driver.quit()