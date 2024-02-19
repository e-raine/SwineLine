import streamlit as st
from PIL import Image

# Changing the web app logo and title
st.set_page_config(
    page_title="SwineLine - Home Page",
    page_icon= Image.open("favicon.ico")
)


st.markdown("""
<header tabindex="-1" data-testid="stHeader" class="st-emotion-cache-1avcm0n ezrtsby2">    
        <nav>
        <ul>
            <li>
            <a href="#">
                <img src="https://pouch.jumpshare.com/preview/ChiIa6vGXXlLBjZXqbOW1g2plJKWohUVtOI1RC2UXR6aIjx8njIQ24kZToBnWgMAzI-lseNKzRlh85Un3yA1RGjiOb8yjQIX4ftrJJm5_hQ" style="width: 64px; height: 64px;">
                <img src="https://pouch.jumpshare.com/preview/UI--6dHDTuYM1qQqFxI1F1dwpmwZrLF8kgGjIPH7QklLllPYduKB_fjGKMEuM-5-mY0GutQna0MI_hcAhp2VNRDizF1SErIs_wEm7WmCdoo" style="width: 113.78px; height: 64px;">
            </a>
            </li>
        </ul>
    </nav>
<header>


""", unsafe_allow_html=True)

# Connect to css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Main")
