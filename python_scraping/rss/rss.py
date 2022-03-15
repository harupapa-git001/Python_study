import csv
import feedparser

with open('articles.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([
        "タイトル",
        "URL",
    ])
    rss = feedparser.parse("https://gigazine.net/news/rss_2.0")

    for entry in rss.entries:
        writer.writerow([
            entry.title,
            entry.link,
        ])