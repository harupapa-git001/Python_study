from bs4 import BeautifulSoup
import requests

url = "https://gigazine.net/"

r = requests.get(url)
heml = r.text
soup = BeautifulSoup(heml, "html.parser")

links = []

items = soup.find_all("a")
for item in items:
    href =item.get("href")
    links.append(href)

print(links)