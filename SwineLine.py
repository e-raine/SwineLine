import streamlit as st

# Title
st.title("Swineline")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.beta_set_page_config(
    page_title="SwineLine"
)
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
