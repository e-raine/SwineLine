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
                <div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://jumpshare.com/embed/t5siRcMSeWWfGaFaraat" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
                <img src="https://pouch.jumpshare.com/preview/UI--6dHDTuYM1qQqFxI1F1dwpmwZrLF8kgGjIPH7QklLllPYduKB_fjGKMEuM-5-h-GKjrMwluNXyctjKgKw-APlM0ji0if2t-U7RdwS02E" style="width: 113.78px; height: 64px;">
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
