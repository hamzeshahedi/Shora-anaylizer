import streamlit as st
import pdfplumber
import re
from transformers import pipeline

# تنظیمات صفحه
st.set_page_config(page_title="تحلیل مصوبات شورا", page_icon="✅", layout="wide")

st.title("سامانه تحلیل مصوبات شورا")

# آپلود فایل
uploaded_file = st.file_uploader("لطفاً فایل PDF مصوبه را بارگذاری کنید", type="pdf")

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    st.subheader("متن کامل مصوبه:")
    st.write(text)

    # استخراج بندهای مصوبه با regex
    st.subheader("بندهای استخراج‌شده:")
    bands = re.findall(r'(?<=\n)[\d۰-۹]+\.?\s+[^\n]+', text)
    for i, band in enumerate(bands, 1):
        st.markdown(f"**{i}. {band}**")

    # دکمه تحلیل مصوبه
    if st.button("تحلیل مصوبه"):
        # تحلیل مفهومی با مدل transformer
        classifier = pipeline("zero-shot-classification", model="Morwared/HerBERT-fa-zsc")

        candidate_labels = [
            "قانون مالیات‌ها",
            "قانون شهرداری‌ها",
            "آیین‌نامه معاملات شهرداری",
            "برنامه توسعه شهری",
            "مصوبات شورای عالی استان‌ها",
            "مقررات ملی ساختمان"
        ]

        st.subheader("تحلیل هر بند نسبت به قوانین بالادستی:")
        for band in bands:
            result = classifier(band, candidate_labels)
            st.markdown(f"**بند:** {band}")
            st.markdown("**تحلیل:**")
            for label, score in zip(result['labels'], result['scores']):
                st.write(f"{label}: {round(score * 100, 2)}%")
            st.markdown("---")
