import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        text = quote.find(class_="text").get_text()
        print(text)
        author = quote.find(class_="author").get_text()
        print(author)

    next_btn = soup.find(class_="next")
    # url = next_btn.find("a") ["href"] if next_btn else NOne
