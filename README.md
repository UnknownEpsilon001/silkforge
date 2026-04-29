# silkforge 🕷️

> Turn raw web data into clean, structured output. Spider the web, forge the data.

Python web scraper & automation toolkit built for freelance automation work.

> ⚠️ **Target site:** This scraper is built specifically for [books.toscrape.com](https://books.toscrape.com/catalogue/) — a practice/sandbox site designed for scraping. It will **not** work on other websites without modifying `parser.py` to match the target site's HTML structure.

## What it does

- Scrapes [books.toscrape.com](https://books.toscrape.com/catalogue/) (all 50 pages, 1000 books)
- Extracts title, price, star rating, and availability per book
- Exports to CSV or Excel
- Supports pagination and partial scraping via CLI flags
- Streamlit UI for demo / portfolio purposes

## Tech stack

- `requests` — HTTP fetching
- `beautifulsoup4` — HTML parsing
- `pandas` — data cleaning & export
- `python-dotenv` — config management
- `streamlit` — demo UI

## Project structure

```
silkforge/
├── config.py         # settings & targets
├── scraper.py        # HTTP fetching + pagination
├── parser.py         # BeautifulSoup data extraction
├── exporter.py       # CSV/Excel output via pandas
├── main.py           # CLI entrypoint
├── app.py            # Streamlit UI (demo)
├── requirements.txt
└── output/           # scraped data lands here
```

## Quickstart

```bash
# create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run scraper (all 50 pages, CSV output)
python main.py

# options
python main.py --pages 5                        # scrape 5 pages only
python main.py --output mydata.csv              # custom filename
python main.py --format excel --output data     # export as .xlsx

# run Streamlit UI
streamlit run app.py
```

## CLI options

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--pages` | `-p` | 50 | Number of pages to scrape |
| `--output` | `-o` | books.csv | Output filename |
| `--format` | `-f` | csv | Export format: `csv` or `excel` |

## Output columns

| Column | Example |
|--------|---------|
| title | A Light in the Attic |
| price | £51.77 |
| rating | 3 |
| available | In stock |

## Support

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/unknownaimo)

## License

MIT — see [LICENSE](LICENSE)

## Author

Leo (Unknown Aimo) — [@UnknownEpsilon001](https://github.com/UnknownEpsilon001)
