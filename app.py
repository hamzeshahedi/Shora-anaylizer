
import streamlit as st
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# طھط§ط¨ط¹ ط§ط³طھط®ط±ط§ط¬ ظ…طھظ† ط§ط² PDF
def extract_text_from_pdf(file):
    doc = fitz.open(file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# طھط§ط¨ط¹ ط§ط³طھط®ط±ط§ط¬ ظ…طھظ† ط§ط² طھطµظˆغŒط±
def extract_text_from_image(file):
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return text

# ط§ظ¾ Streamlit
st.title("طھط­ظ„غŒظ„ ظ…طµظˆط¨ط§طھ ط´ظˆط±ط§ظ‡ط§غŒ ط§ط³ظ„ط§ظ…غŒ")
st.write("ظ„ط·ظپط§ظ‹ ظپط§غŒظ„ PDF غŒط§ طھطµظˆغŒط± ط±ط§ ط¨ط±ط§غŒ طھط­ظ„غŒظ„ ظˆط§ط±ط¯ ع©ظ†غŒط¯:")

# ط¢ظ¾ظ„ظˆط¯ ظپط§غŒظ„
uploaded_file = st.file_uploader("ظپط§غŒظ„ ط®ظˆط¯ ط±ط§ ط¢ظ¾ظ„ظˆط¯ ع©ظ†غŒط¯", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    # ظ†ظ…ط§غŒط´ ظ†ط§ظ… ظپط§غŒظ„
    st.write(f"ظپط§غŒظ„ {uploaded_file.name} ط¢ظ¾ظ„ظˆط¯ ط´ط¯!")

    # ط§ع¯ط± ظپط§غŒظ„ PDF ط¨ظˆط¯
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
        st.write("ظ…طھظ† ط§ط³طھط®ط±ط§ط¬ ط´ط¯ظ‡ ط§ط² PDF:")
        st.write(text)

    # ط§ع¯ط± ظپط§غŒظ„ طھطµظˆغŒط± ط¨ظˆط¯
    elif uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:
        text = extract_text_from_image(uploaded_file)
        st.write("ظ…طھظ† ط§ط³طھط®ط±ط§ط¬ ط´ط¯ظ‡ ط§ط² طھطµظˆغŒط±:")
        st.write(text)
