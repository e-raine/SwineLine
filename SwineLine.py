from PIL import Image
import streamlit as st
import favicon
 

st.set_page_config(
    page_title="SwineLine",
    page_icon= Image.open(favicon)
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

