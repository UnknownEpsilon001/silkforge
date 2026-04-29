import os
import argparse
from scraper import get_all_pages
from parser import parse_all
from exporter import export_csv, export_excel
from config import MAX_PAGES


def parse_args():
    parser = argparse.ArgumentParser(description="silkforge web scraper")
    parser.add_argument("--pages", "-p", type=int, default=MAX_PAGES, help="Number of pages to scrape")
    parser.add_argument("--output", "-o", type=str, default="books.csv", help="Output filename")
    parser.add_argument("--format", "-f", choices=["csv", "excel"], default="csv", help="Export format")
    return parser.parse_args()


def main():
    args = parse_args()
    print("Starting silkforge scraper...")

    pages = get_all_pages(max_pages=args.pages)
    books = parse_all(pages)

    if args.format == "excel":
        export_excel(books, filename=os.path.splitext(args.output)[0] + ".xlsx")
    else:
        export_csv(books, filename=args.output)

    print(f"Done. {len(books)} books scraped.")


if __name__ == "__main__":
    main()
