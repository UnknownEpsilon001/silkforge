from scraper import get_all_pages
from parser import parse_all
from exporter import export_csv


def main():
    print("Starting silkforge scraper...")

    # 1. fetch
    pages = get_all_pages()

    # 2. parse
    books = parse_all(pages)

    # 3. export
    export_csv(books)

    print(f"Done. {len(books)} books scraped.")


if __name__ == "__main__":
    main()
