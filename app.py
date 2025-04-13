import streamlit as st
import pytesseract
from PIL import Image
import re

st.title("📷 Image Metrics Reader (OCR-based)")
st.write("Upload an image (handwritten or printed) with accuracy, precision, recall, and F1-score formulas or values.")

uploaded_img = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.subheader("🔍 Extracted Text")
    text = pytesseract.image_to_string(image)
    st.text(text)

    # Try regex to extract metric formulas/values
    st.subheader("📊 Extracted Metrics (if found)")

    accuracy = re.search(r"Accuracy\s*=\s*(.*)", text, re.IGNORECASE)
    precision = re.search(r"Precision\s*=\s*(.*)", text, re.IGNORECASE)
    recall = re.search(r"Recall\s*=\s*(.*)", text, re.IGNORECASE)
    f1 = re.search(r"F1\s*score\s*=\s*(.*)", text, re.IGNORECASE)

    if accuracy:
        st.markdown(f"**Accuracy:** `{accuracy.group(1).strip()}`")
    if precision:
        st.markdown(f"**Precision:** `{precision.group(1).strip()}`")
    if recall:
        st.markdown(f"**Recall:** `{recall.group(1).strip()}`")
    if f1:
        st.markdown(f"**F1 Score:** `{f1.group(1).strip()}`")

    if not any([accuracy, precision, recall, f1]):
        st.warning("Could not extract metrics. Try uploading a clearer image.")
