import streamlit as st
import re

# خواندن فایل قوانین از ریشه پروژه
def load_laws():
    try:
        with open("sample_laws.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "فایل قوانین یافت نشد. لطفاً sample_laws.txt را در ریشه پروژه قرار دهید."

# تطبیق هر خط از مصوبه با قوانین
def analyze_resolution(resolution, laws):
    results = []
    for line in resolution.split("\n"):
        if not line.strip():
            continue
        match = re.search(re.escape(line.strip()), laws)
        if match:
            results.append(f"✔️ انطباق یافت: {line}")
        else:
            results.append(f"❌ مغایرت یا عدم انطباق: {line}")
    return results

# رابط کاربری استریم‌لیت
st.title("تحلیل هوشمند مصوبات شورا با قوانین بالادستی")

laws_text = load_laws()

st.write("متن قوانین بارگذاری شده:")
st.write(laws_text[:500])  # نمایش اولین 500 کاراکتر از قوانین برای بررسی

resolution_input = st.text_area("متن مصوبه را وارد کنید (هر خط جداگانه بررسی می‌شود):", height=300)

if st.button("تحلیل مصوبه"):
    if not resolution_input.strip():
        st.warning("لطفاً ابتدا یک متن مصوبه وارد کنید.")
    else:
        st.info("در حال تحلیل مصوبه...")
        analysis = analyze_resolution(resolution_input, laws_text)
        for result in analysis:
            st.write(result)
