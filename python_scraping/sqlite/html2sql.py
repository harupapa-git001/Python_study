from bs4 import BeautifulSoup
import sqlite3

#データベースに接続
con = sqlite3.connect("items.db")

#カーソルを取り出す
cursor = con.cursor()

#もしテーブルが存在しない場合は作成
cursor.execute("CREATE TABLE IF NOT EXISTS items (title TEXT, price INTEGER, count INTEGER)")

#HTMLファイルを開く
with open('index.html', 'r') as html:
    soup = BeautifulSoup(html.read(), "html.parser")
    trs = soup.find_all("tr")

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            #データを挿入
            cursor.execute("INSERT INTO items VALUES(?, ?, ?)", list(map(lambda i: i.string, tds)))

    #変更を反映させる
    con.commit()
    con.close()
    