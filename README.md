# silkforge 🕷️

> Turn raw web data into clean, structured output. Spider the web, forge the data.

Python web scraper & automation toolkit built for freelance automation work.

## What it does

- Scrapes websites (static HTML — no JS required)
- Cleans and structures extracted data
- Exports to CSV / Excel
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
├── scraper.py        # core scraping logic
├── parser.py         # data extraction & cleaning
├── exporter.py       # CSV/Excel output
├── config.py         # settings & targets
├── requirements.txt
└── output/           # scraped data lands here
```

## Quickstart

```bash
# install deps
pip install -r requirements.txt

# run scraper
python scraper.py --url <target> --pages 5 --output data.csv
```

## Use cases (freelance services)

- Product price monitoring
- E-commerce catalog extraction
- News / article archiving
- Lead list generation
- Scheduled data pipelines

## Author

[@UnknownEpsilon001](https://github.com/UnknownEpsilon001) — Python automation & scripting
