
import streamlit as st
from transformers import pipeline
import pdfplumber
import tempfile
import os

# مدل پیش‌فرض برای تحلیل متون فارسی
@st.cache_resource
def load_model():
    return pipeline("zero-shot-classification",
                    model="HooshvareLab/bert-fa-base-uncased-clf")

nlp = load_model()

# تابع برای استخراج متن از PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "
"
    return text

# رابط کاربری
st.set_page_config(page_title="تحلیل مصوبات شورا", layout="wide")
st.title("تحلیل مصوبات شورای اسلامی")

uploaded_file = st.file_uploader("فایل مصوبه را بارگذاری کنید (PDF یا تایپ دستی)", type=["pdf"])
manual_text = st.text_area("یا متن مصوبه را اینجا وارد کنید:", height=300)

if uploaded_file or manual_text:
    st.subheader("نتایج تحلیل")
    
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            text = extract_text_from_pdf(tmp_file.name)
            os.unlink(tmp_file.name)
    else:
        text = manual_text

    candidate_labels = ["مغایرت با قوانین بالادستی", "مطابقت با قوانین", "نیاز به بررسی بیشتر"]
    
    for i, line in enumerate(text.split("
")):
        if line.strip():
            result = nlp(line, candidate_labels)
            st.markdown(f"**{i+1}. {line.strip()}**")
            st.write({label: f"{score:.2f}" for label, score in zip(result['labels'], result['scores'])})
            st.markdown("---")
