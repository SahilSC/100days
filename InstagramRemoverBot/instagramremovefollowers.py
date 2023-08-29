#You should install the selenium python package (IDEs like PyCharm will allow you to do this really easily by hovering over the uninstalled packages)
#Note you CANNOT SWITCH TO ANOTHER TAB while the Instagram Unfollower Bot is doing its job!
#You must keep the automated web browser that pops open OPEN. You must have Chrome installed
#Please insert your instagram username on line 15, instagram password on line 16
#The program will print the instagram handles of the people you follow that don't follow you back
#If you set line 17 to True, then the program will automatically unfollow the people that you follow that don't follow you back


from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

#SETTINGS
INSTA_USERNAME = USERNAME
INSTA_PASSWORD = PASSWORD  # instead of using os.environ, just replace with password
AUTO_UNFOLLOW = True

driver = webdriver.Chrome()

#given a HTML div scroll element and appropriate follower/following button, this method retrieves all instagram handles
def retrieve_handle_list(scrollable_element):
    global driver
    scroll(scrollable_element)
    insta_handles = [tag.text for tag in driver.find_elements(By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1')]
    return insta_handles

def scroll(scrollable_element):
    while True:
        start_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)
        time.sleep(2)
        end_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)
        # breaks scrolling
        if end_height == start_height:
            break

def scroll_to_element(element):
    driver.execute_script("arguments[0].scrollIntoView(true)", element)

def unfollow_list(followers, following):
    unfollowlist = []
    index = []
    for ind in range(0, len(following)):
        insta_handle = following[ind]
        if insta_handle not in followers:
            unfollowlist.append(insta_handle)
            index.append(ind)
    return (unfollowlist, index)


url = 'https://instagram.com'
driver.get(url)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(INSTA_USERNAME)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(INSTA_PASSWORD)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)

try:  # checks if "Turn on notification pop-up appears"
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
except:
    pass

driver.maximize_window()
# Now, go to pfp
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div/div[2]/div/div').click()
time.sleep(5)

#enters following pages, scrolls, exists following page
followingtag = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
followingtag.click()
time.sleep(5)
following_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
following_list = retrieve_handle_list(following_page)
driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Close"]').click()

#enters followers page, scrolls, exits followers page
followerstag = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followerstag.click()
time.sleep(5)
followers_page = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
followers_list = retrieve_handle_list(followers_page)
driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Close"]').click()


(unfollowlist, unfollowindex) = unfollow_list(followers_list, following_list)

print(unfollowlist)

if AUTO_UNFOLLOW:
    followingtag.click()
    time.sleep(5)
    # scroll(following_page)
    followingbuttons = driver.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acat._aj1-')
    len(followingbuttons)
    unfollowbuttons = [followingbuttons[i] for i in unfollowindex]
    for button in unfollowbuttons:
        scroll_to_element(button)
        button.click()
        driver.find_element(By.CSS_SELECTOR, "button._a9--._a9-_").click()


