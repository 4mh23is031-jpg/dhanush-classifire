import streamlit as st
import json
from classifier import classify_po

st.set_page_config(page_title="PO Category Classifier", layout="centered")

st.title("📦 PO L1–L2–L3 Classifier")

po_description = st.text_area("PO Description", height=120)
supplier = st.text_input("Supplier (optional)")

if st.button("Classify"):
    if not po_description.strip():
        st.warning("Please enter a PO description.")
    else:
        with st.spinner("Classifying..."):
            result = classify_po(po_description, supplier)

        try:
            st.json(json.loads(result))
        except Exception:
            st.error("Invalid model response")
            st.text(result)
