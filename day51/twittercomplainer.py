from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
user = os.environ['TWITTER_USERNAME']
password = os.environ['TWITTER_PASSWORD']

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, 'span.start-text').click()
        time.sleep(70)
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'a.close-btn').click()
        except:
            pass
        self.down = float(self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.tweet_at_provider()

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            msg = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}/{PROMISED_UP}?"
            self.driver.get('https://twitter.com')
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
            time.sleep(5)
            user_ele = self.driver.find_element(By.NAME, 'text')
            user_ele.send_keys(user)
            user_ele.send_keys(Keys.ENTER)
            time.sleep(.5)
            pass_ele = self.driver.find_element(By.NAME, 'password')
            pass_ele.send_keys(password)
            pass_ele.send_keys(Keys.ENTER)
            time.sleep(4)
            start_ele = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
            start_ele.send_keys(msg[0:1])
            remaining_ele = self.driver.find_element(By.CSS_SELECTOR, 'span[data-text="true"]')
            remaining_ele.send_keys(msg[1:])
            self.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
tweet_complainer = InternetSpeedTwitterBot()
tweet_complainer.get_internet_speed()
tweet_complainer.tweet_at_provider()
# msg = f"Hey Internet Provider, why is my internet speed 12down/23up when I pay for {PROMISED_DOWN}/{PROMISED_UP}?"
# driver = webdriver.Chrome()
# twitter = 'https://twitter.com'
# driver.get(twitter)
# driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
# time.sleep(5)
# user_ele = driver.find_element(By.NAME, 'text')
# user_ele.send_keys(user)
# user_ele.send_keys(Keys.ENTER)
# time.sleep(.5)
# pass_ele = driver.find_element(By.NAME, 'password')
# pass_ele.send_keys(password)
# pass_ele.send_keys(Keys.ENTER)
# time.sleep(4)
# start_ele = driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
# start_ele.send_keys(msg[0:1])
# remaining_ele = driver.find_element(By.CSS_SELECTOR,'span[data-text="true"]')
# remaining_ele.send_keys(msg[1:])
# driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()