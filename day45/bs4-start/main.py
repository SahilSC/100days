from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
names = [tag.getText() for tag in soup.select('span.titleline a')]
links = [tag.get('href') for tag in soup.select('span.titleline a')]
points = [int(tag.getText().split()[0]) for tag in soup.select('span.score')]
print(points)
maxpoint = -1
ind = 0
for _ in range(0, len(points)):
    point = points[_]
    if point > maxpoint:
        ind = _
        maxpoint = point

print(f"Max points: {maxpoint}\nHeadline: {names[ind]}\nWebsite: {links[ind]}")

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# name = soup.find(name="h1", id="name")
# college = soup.select_one(selector="p a")
# print(college.name)