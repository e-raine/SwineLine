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
        <img src="https://pouch.jumpshare.com/preview/ex0FNyTDEcWBbtj58-j0dbIM2se2Uzhu576DMpkE97NTwyPtZ4y1oUQoxm-IsK6isoVnuMKa6P8P5ZSY7hTubEBAI8FhnPOOcOYfHHtqX8M">
    </a>
  </li>
  </ul>
  </nav>
</header>
""", unsafe_allow_html=True)

# Connect to css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
