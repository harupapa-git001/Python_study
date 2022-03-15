from bs4 import BeautifulSoup
import requests

url = "https://gigazine.net/news/20190121-elsevier-editors-rival-open-access-journal"

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("img")

number = 1

for item in items:
    try:
        src = item.get("src")
        print(src)
        if src == None:
            continue

        r = requests.get(src)
        with open("image" + str(number) + ".png", "wb") as file:
            file.write(r.content)

    except Exception as e:
        print(e)

    number += 1