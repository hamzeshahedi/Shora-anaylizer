import streamlit as st
import os

# بررسی اینکه فایل قوانین واقعاً وجود داره یا نه
def load_laws():
    if os.path.exists("sample_laws.txt"):
        with open("sample_laws.txt", "r", encoding="utf-8") as f:
            return f.read()
    else:
        return None

# بررسی ساده هر خط مصوبه
def analyze_resolution(resolution, laws):
    results = []
    for line in resolution.split("\n"):
        if line.strip() == "":
            continue
        if line.strip() in laws:
            results.append(f"✔️ انطباق یافت: {line}")
        else:
            results.append(f"❌ مغایرت یا عدم انطباق: {line}")
    return results

# UI
st.title("تحلیل مصوبات با قوانین بالادستی")

laws_text = load_laws()

if laws_text is None:
    st.error("فایل قوانین (sample_laws.txt) پیدا نشد. لطفاً آن را در ریشه پروژه قرار دهید.")
else:
    st.success("فایل قوانین با موفقیت بارگذاری شد.")

    resolution_input = st.text_area("متن مصوبه را وارد کنید (هر خط جداگانه بررسی می‌شود):")

    if st.button("تحلیل مصوبه"):
        if not resolution_input.strip():
            st.warning("لطفاً یک متن مصوبه وارد کنید.")
        else:
            st.info("در حال تحلیل مصوبه...")
            result = analyze_resolution(resolution_input, laws_text)
            st.write("**نتایج:**")
            for line in result:
                st.write(line)
