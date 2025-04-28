# app.py

import streamlit as st
from crawler import crawl_site
from extractor import extract_modules_and_submodules
import json

st.title("Pulse-AI Module Extraction Agent")

st.write("""
Enter one or more help documentation URLs (one per line) below, and click "Extract Modules and Submodules".
""")

# User input
urls_input = st.text_area("Enter URLs here:")

# Button
if st.button("Extract Modules and Submodules"):
    if urls_input.strip() == "":
        st.error("Please enter at least one URL.")
    else:
        urls = urls_input.strip().splitlines()
        final_output = []

        for url in urls:
            st.write(f"Processing URL: {url} ...")
            crawled_pages = crawl_site(url, max_pages=20)

            for page_url, page_text, soup in crawled_pages:
                modules = extract_modules_and_submodules(soup)
                if modules:
                    final_output.append(modules)

        # Show JSON output
        st.subheader("Extracted JSON Output:")
        st.json(final_output)

        # Optionally, save to a JSON file
        with open("output.json", "w") as f:
            json.dump(final_output, f, indent=2)

        st.success("Extraction completed! Output also saved to 'output.json' file.")