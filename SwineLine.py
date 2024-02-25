import pandas as pd
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
                <img src="https://res.cloudinary.com/dxyyqx3l6/image/upload/v1708828402/Logo.svg" style="width: 64px; height: 64px;">
                <img src="https://res.cloudinary.com/dxyyqx3l6/image/upload/v1708828270/Banner.svg" style="width: 113.78px; height: 64px;">
            </a>
            </li>
        </ul>
    </nav>
<header>


""", unsafe_allow_html=True)

# Connect to css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("DashBoard")

df = pd.read_excel(
    io="Data.xlsx",
    engine="openpyxl",
    sheet_name="Sheet2",
    usecols="B:D",
)

st.dataframe(df)