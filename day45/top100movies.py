from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
url = 'https://www.empireonline.com/movies/features/best-movies-2/'

with webdriver.Chrome(options = chrome_options) as driver:
    driver.get('https://www.empireonline.com/movies/features/best-movies-2/')
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    names = [tag.getText() for tag in soup.find_all("h3")]
    with open("topmovies.txt", "w") as file:
        for _ in range(len(names)-1, -1, -1):
            file.write(names[_] +"\n")
