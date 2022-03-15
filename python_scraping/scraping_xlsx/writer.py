from bs4 import BeautifulSoup
from openpyxl import Workbook

book = Workbook()
sheet = book.active

with open('index.html', 'r') as html:
    soup = BeautifulSoup(html.read(), "html.parser")
    trs = soup.find_all("tr")

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            sheet.append(list(map(lambda i: i.string, tds)))

        elif tr.find_all("th"):
            ths = tr.find_all("th")
            sheet.append(list(map(lambda i: i.string, ths)))

book.save("zaiko.xlsx")