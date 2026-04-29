import pandas as pd
import os
from config import OUTPUT_DIR


def export_csv(books, filename="books.csv"):
    """Save list of book dicts to CSV."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)

    df = pd.DataFrame(books)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"Saved {len(books)} rows to {path}")


def export_excel(books, filename="books.xlsx"):
    """Save list of book dicts to Excel."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)

    df = pd.DataFrame(books)
    df.to_excel(path, index=False)
    print(f"Saved {len(books)} rows to {path}")

