from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="SwineLine",
)

hide_st_style = """
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Title
st.title("Swineline")

# header
st.header("This is the Heading")

# subheader
st.subheader("This is the subheading")

# text
st.text("Hello World!")

# success, info
st.success("Executed successfully")
st.info("This is an information")
st.warning("This is a warning")
st.error("This is an error")
