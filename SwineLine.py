import streamlit as st
from PIL import Image

# Changing the web app logo and title
st.set_page_config(
    page_title="SwineLine",
    page_icon= Image.open("favicon.ico")
)


st.markdown("""
<header tabindex="-1" data-testid="stHeader" class="st-emotion-cache-1avcm0n ezrtsby2">
        <ul>
            <li class="Lev-1">
                <a href="">Level-1</a>
                <ul>
                    <li><a href="https://swineline.streamlit.app/~/+/">Link 1</a></li>
                    <li><a href="https://swineline.streamlit.app/~/+/marketplace">Link 2</a></li>
                </ul>
            </li>
            <li>
                <div class="logo">
                    <a href="#">
                    <img src="https://pouch.jumpshare.com/preview/ChiIa6vGXXlLBjZXqbOW1g2plJKWohUVtOI1RC2UXR6aIjx8njIQ24kZToBnWgMAyFb93RkyHQzbjCH_oylQni--7bgpO1xY3C4xkXUfm4s" style="width: 3.5rem; height: 3.5rem;">
                    <img src="https://pouch.jumpshare.com/preview/UI--6dHDTuYM1qQqFxI1F1dwpmwZrLF8kgGjIPH7QklLllPYduKB_fjGKMEuM-5-Fyh0q_s75f28xrrTzp5nT1IwJ-AR6DFQHBOxFbY-Kg4" style="width: 8rem; height: 4.5rem;">
                    </a>
                </div>
            </li>
        </ul>
</header>
            
""", unsafe_allow_html=True)

# Connect to css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


