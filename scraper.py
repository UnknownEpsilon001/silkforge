import requests
import time
from config import BASE_URL, MAX_PAGES, REQUEST_DELAY


def get_page(url):
    """Fetch HTML from a single URL. Returns response text or None on failure."""
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return res.text
        return None
    except requests.exceptions.RequestException:
        print(f"Error fetching {url}")
        return None


def get_all_pages(max_pages=MAX_PAGES):
    """Crawl all pages. Returns list of HTML strings."""
    pages = []

    for page_num in range(1, max_pages + 1):
        url = f"{BASE_URL}page-{page_num}.html"
        html = get_page(url)
        if html:
            pages.append(html)
            print(f"Progress: {page_num}/{max_pages}")
        time.sleep(REQUEST_DELAY)

    return pages
