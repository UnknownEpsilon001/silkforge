# silkforge — Claude Context

## Project
Python web scraper & automation toolkit. Target: `books.toscrape.com` (practice site).
Output: clean CSV. Supports pagination. Built for freelance portfolio.

**Goal:** Showcase Python automation skills for รับเขียน Python Script & Automation freelance work.

## Planned file structure
```
silkforge/
├── scraper.py        # HTTP fetching + pagination
├── parser.py         # BeautifulSoup data extraction
├── exporter.py       # CSV/Excel output via pandas
├── config.py         # target URL, settings
├── requirements.txt
└── output/           # scraped CSVs land here
```

## Tech
- `requests` — fetch HTML
- `beautifulsoup4` — parse HTML
- `pandas` — clean + export data
- `python-dotenv` — config

## User context
- GitHub: UnknownEpsilon001
- First year ปวส student, heading to CE
- Stack otherwise: Vue 3 + Node.js (other projects)
- Learning style: step-by-step, wants to understand WHY not just copy-paste
- Casual vibe, short direct answers preferred

## How to work with user
- Explain each file/function before writing it
- Use "Learn by Doing" — ask user to implement small meaningful pieces
- Don't dump everything at once — build one file at a time
- After each file: commit to git

## Other active projects
- ApplyHQ: full-stack job tracker, Vue3+Node+SQLite, at `C:\Users\UNKNOWN\Documents\GitHub\ApplyHQ`
