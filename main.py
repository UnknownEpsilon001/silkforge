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


BANNER = r"""
  _____ _ _ _     __
 / ____(_) | |   / _|
| (___  _| | | _| |_ ___  _ __ __ _  ___
 \___ \| | | |/ /  _/ _ \| '__/ _` |/ _ \
 ____) | | |   <| || (_) | | | (_| |  __/
|_____/|_|_|_|\_\_| \___/|_|  \__, |\___|
                                __/ |
  web scraper toolkit          |___/  v1.0
"""


def main():
    args = parse_args()
    print(BANNER)
    print(f"  target  : books.toscrape.com")
    print(f"  pages   : {args.pages}")
    print(f"  output  : {args.output}")
    print(f"  format  : {args.format}")
    print("-" * 40)

    pages = get_all_pages(max_pages=args.pages)
    books = parse_all(pages)

    if args.format == "excel":
        export_excel(books, filename=os.path.splitext(args.output)[0] + ".xlsx")
    else:
        export_csv(books, filename=args.output)

    print(f"Done. {len(books)} books scraped.")


if __name__ == "__main__":
    main()
