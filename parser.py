from bs4 import BeautifulSoup


RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_page(html):
    """Extract book data from one page of HTML. Returns list of dicts."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for article in soup.find_all("article", class_="product_pod"):
        book = {
            "title": article.h3.a["title"],
            "price": article.find("p", class_="price_color").text.strip(),
            "rating": RATING_MAP.get(article.p["class"][1], 0),
            "available": article.find("p", class_="instock availability").text.strip(),
        }
        books.append(book)

    return books


def parse_all(pages):
    """Run parse_page on every page. Returns flat list of all books."""
    all_books = []
    for html in pages:
        all_books.extend(parse_page(html))
    return all_books
