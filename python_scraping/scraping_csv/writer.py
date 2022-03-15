from bs4 import BeautifulSoup
import csv

with open('index.html', 'r') as html:
    soup = BeautifulSoup(html.read(), "html.parser")
    trs = soup.find_all("tr")

    with open('zaiko.csv', 'w') as file:
        writer = csv.writer(file)
        for tr in trs:
            tds = tr.find_all("td")
            if tds:
                writer.writerow(map(lambda i: i.string, tds))

            elif tr.find_all("th"):
                ths = tr.find_all("th")
                writer.writerow(map(lambda i: i.string, ths))