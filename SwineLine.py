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
        <img src="https://scontent.fcgm1-1.fna.fbcdn.net/v/t39.30808-6/426405471_122097138446217431_8065067454837553768_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeFIeH8sRiafbnX58D-3zpvPUDm-yH6FMftQOb7IfoUx-3ZVVQMVujEsad8YjO5eL1ssYD8yUwYgdf0RYRlG_IY7&_nc_ohc=xnaQJVlKHcEAX-L4iZh&_nc_ht=scontent.fcgm1-1.fna&oh=00_AfBBgzJDNDaO150NeZnh-qLw9-eSm3knobjPc6dABwne8A&oe=65D5F92C">
    </a>
  </li>
  </ul>
  </nav>
</header>
""", unsafe_allow_html=True)

# Connect to css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
