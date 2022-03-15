import sqlite3

#データベースに接続
con = sqlite3.connect("items.db")

cursor = con.cursor()

items = cursor.execute("SELECT * FROM items")

for item in items:
    print(item)
    