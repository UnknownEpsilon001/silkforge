# silkforge 🕷️

> Turn raw web data into clean, structured output. Spider the web, forge the data.

Python web scraper & automation toolkit built for freelance automation work.

## What it does

- Scrapes websites (static HTML — no JS required)
- Cleans and structures extracted data
- Exports to CSV or Excel
- Supports multi-page pagination
- Runs from CLI — no UI needed

## Tech stack

- `requests` — HTTP fetching
- `beautifulsoup4` — HTML parsing
- `pandas` — data cleaning & export
- `python-dotenv` — config management

## Project structure

```
silkforge/
├── config.py         # settings & targets
├── scraper.py        # HTTP fetching + pagination
├── parser.py         # BeautifulSoup data extraction
├── exporter.py       # CSV/Excel output via pandas
├── main.py           # CLI entrypoint
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
```

## CLI options

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--pages` | `-p` | 50 | Number of pages to scrape |
| `--output` | `-o` | books.csv | Output filename |
| `--format` | `-f` | csv | Export format: `csv` or `excel` |

## Use cases (freelance services)

- Product price monitoring
- E-commerce catalog extraction
- News / article archiving
- Lead list generation
- Scheduled data pipelines

## License

MIT — see [LICENSE](LICENSE)

## Author

Leo (Unknown Aimo) — [@UnknownEpsilon001](https://github.com/UnknownEpsilon001)
