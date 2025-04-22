import streamlit as st
from transformers import pipeline
from huggingface_hub import login

# وارد کردن توکن Hugging Face
login(token="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")

# استفاده از مدل Hugging Face parsBERT برای تجزیه مفهومی متن
nlp = pipeline("zero-shot-classification", model="HooshvareLab/bert-fa-base-uncased-clf")

# این تابع برای تجزیه متن به مفاهیم مختلف و شناسایی موضوعات استفاده می‌شود.
def analyze_concepts(text):
    categories = ["افتتاح حساب", "تصویب بودجه", "پروژه‌های عمرانی", "آیین‌نامه", "قوانین شهرداری"]
    results = nlp(text, candidate_labels=categories)
    return results

# رابط کاربری Streamlit
st.title("تحلیل هوشمند مصوبات شورا با تحلیل مفهومی")

st.write("لطفاً مصوبه را وارد کنید تا تحلیل مفهومی و تطبیقی انجام شود:")

# ورودی مصوبه از کاربر
resolution_input = st.text_area("متن مصوبه را وارد کنید:", height=300)

if st.button("تحلیل مصوبه"):
    if not resolution_input.strip():
        st.warning("لطفاً یک متن مصوبه وارد کنید.")
    else:
        st.info("در حال تحلیل مصوبه...")
        
        # تحلیل مفهومی مصوبه
        concepts = analyze_concepts(resolution_input)
        st.write("**نتایج تحلیل مفهومی:**")
        st.write(f"موضوع اصلی: {concepts['labels'][0]}")
        st.write(f"اعتماد مدل به این تحلیل: {concepts['scores'][0] * 100:.2f}%")
