import streamlit as st
import pandas as pd
import io
from scraper import get_all_pages
from parser import parse_all

st.set_page_config(page_title="silkforge", page_icon="🕷️", layout="wide")

st.title("🕷️ silkforge")
st.caption("Web scraper — books.toscrape.com")

with st.sidebar:
    st.header("Settings")
    pages = st.slider("Pages to scrape", min_value=1, max_value=50, value=5)
    fmt = st.radio("Export format", ["CSV", "Excel"])
    run = st.button("Run scraper", type="primary", use_container_width=True)

if run:
    with st.spinner(f"Scraping {pages} page(s)..."):
        html_pages = get_all_pages(max_pages=pages)
        books = parse_all(html_pages)
        df = pd.DataFrame(books)

    st.success(f"Scraped {len(df)} books from {pages} page(s)")
    st.dataframe(df, use_container_width=True)

    if fmt == "CSV":
        data = df.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")
        st.download_button("Download CSV", data, file_name="books.csv", mime="text/csv")
    else:
        buf = io.BytesIO()
        df.to_excel(buf, index=False)
        st.download_button("Download Excel", buf.getvalue(), file_name="books.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
else:
    st.info("Configure settings in the sidebar, then click **Run scraper**.")
