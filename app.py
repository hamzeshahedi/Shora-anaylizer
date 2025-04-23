
import streamlit as st
import pdfplumber

st.set_page_config(page_title="تحلیل مصوبات", layout="wide")
st.title("سامانه ساده تحلیل مصوبه شورا")

uploaded_file = st.file_uploader("فایل PDF مصوبه را بارگذاری کنید:", type="pdf")

if uploaded_file:
    st.success("فایل با موفقیت بارگذاری شد.")

    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    st.subheader("متن مصوبه:")
    st.write(text)

    if st.button("تحلیل مصوبه"):
        st.subheader("نتایج تحلیل (شبیه‌سازی ساده):")
        for i, line in enumerate(text.split("\n")):
            if line.strip():
                st.markdown(f"**{i+1}.** {line.strip()}")
                st.write("وضعیت: بررسی شد (شبیه‌سازی)")
