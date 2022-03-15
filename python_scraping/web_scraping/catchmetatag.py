from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

book = Workbook()
sheet = book.active

links = [
    "https://gigazine.net/news/20190114-basketball-in-tibet/",
    "https://gigazine.net/news/20190114-airpower-charging-producing-start/",
    "https://gigazine.net/news/20190114-undistracted-chrome-extension/",
    "https://gigazine.net/news/20190114-ipad-mini-4s/",
    "https://gigazine.net/news/20190114-multicopy/"
]

columns = [
    "og:title",
    "og:url",
    "og:image"
]

row_id = 2

sheet.append(columns)

for link in links:
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("meta")

    for item in items:
        row = []
        prop = item.get("property")
        content = item.get("content")

        if content == None:
            continue

        if prop in columns:
            print(content)
            _ = sheet.cell(column=(columns.index(prop) + 1), row=row_id, value=content)

    row_id += 1

book.save("meta.xlsx")