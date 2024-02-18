import streamlit as st
from PIL import Image

# Changing the web app logo and title
st.set_page_config(
    page_title="SwineLine",
    page_icon= Image.open("favicon.ico")
)


st.markdown("""
<header tabindex="-1" data-testid="stHeader" class="st-emotion-cache-1avcm0n ezrtsby2">
  <nav>
  <ul>
  <li>
    <a href="#">
      <img src="https://github.com/e-raine/SwineLine/blob/main/images/SVG/Swineline%20Header_Pink.svg" alt="SwineLine Logo" width="30" height="24">
    </a>
  </li>
  </ul>
  </nav>
</header>
""", unsafe_allow_html=True)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Title 
st.title("SwineLine")