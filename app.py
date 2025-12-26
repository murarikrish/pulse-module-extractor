import streamlit as st
import json
from module_extractor.pipeline import ModuleExtractionPipeline

st.title("Pulse – Module Extraction AI Agent")

urls = st.text_area("Enter help documentation URLs (one per line)").splitlines()

if st.button("Extract Modules"):
    pipeline = ModuleExtractionPipeline()
    result = pipeline.run(urls)

    st.json(result)

    with open("output/result.json", "w") as f:
        json.dump(result, f, indent=2)

    st.success("Extraction complete. File saved to output/result.json")
