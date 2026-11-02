
import requests
from bs4 import BeautifulSoup


def fetch_data():
    """Fetch books from Books to Scrape."""
    url = "https://books.toscrape.com/"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").text
        books.append({"title": title, "price": price})

    return books
