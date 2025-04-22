
import streamlit as st

# تنظیم فونت فارسی با CSS
st.markdown("""
    <style>
    @font-face {
      font-family: 'Vazir';
      src: url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font/dist/Vazir.woff2') format('woff2');
    }
    html, body, [class*="css"]  {
      font-family: 'Vazir', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان و توضیحات
st.title("بررسی انطباق مصوبات شورای اسلامی با قوانین")
st.write("لطفاً مصوبه مورد نظر را وارد کرده یا فایل آن را بارگذاری نمایید:")

# فرم ورودی
uploaded_file = st.file_uploader("فایل مصوبه (PDF, JPG, PNG)", type=["pdf", "jpg", "jpeg", "png"])
text_input = st.text_area("یا متن مصوبه را اینجا وارد کنید")

# دکمه ارسال
if st.button("تحلیل کن"):
    if uploaded_file:
        st.success("فایل با موفقیت بارگذاری شد. تحلیل در حال انجام است...")
        # اینجا منطق تحلیل فایل را اضافه کنید
    elif text_input.strip():
        st.success("متن دریافت شد. تحلیل در حال انجام است...")
        # اینجا منطق تحلیل متن را اضافه کنید
    else:
        st.error("لطفاً یک فایل انتخاب کنید یا متن وارد نمایید.")
