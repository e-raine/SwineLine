from PIL import Image
import streamlit as st

im = Image.open("Images\PNG\Swineline Header_Light.jpg")
st.set_page_config(
    page_title="SwineLine",
    page_icon= im

)

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
