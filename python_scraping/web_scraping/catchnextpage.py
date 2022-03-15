import csv
import requests
from bs4 import BeautifulSoup

url = "https://gigazine.net/"

with open('articles.csv', 'w') as file:
    writer = csv.writer(file)

    for i in range(5):
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")

        next = soup.find("div", {"id": "nextpage"})

        url = next.find("a").attrs["href"]

        cards = soup.find_all("div", {"class":"card"})

        for card in cards:
            title = card.find("h2").text.strip()
            href = card.find("a").attrs["href"]

            writer.writerow([
                title,
                href,
            ])