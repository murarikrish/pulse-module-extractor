import streamlit as st
import json
import os
from module_extractor.pipeline import ModuleExtractionPipeline

st.title("Pulse – Module Extraction AI Agent")

urls_input = st.text_area("Enter help documentation URLs (one per line)")
urls = [u.strip() for u in urls_input.splitlines() if u.strip()]

if st.button("Extract Modules") and urls:
    pipeline = ModuleExtractionPipeline()
    result = pipeline.run(urls)

    # Show output in UI
    st.subheader("Extracted Modules")
    st.json(result)

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Save JSON output
    with open("output/result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    st.success("Extraction complete. File saved to output/result.json")
