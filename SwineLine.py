import streamlit as st
from PIL import Image

# Changing the web app logo and title
st.set_page_config(
    page_title="SwineLine",
    page_icon= Image.open("favicon.ico")
)


st.markdown("""
    <script type="text/javascript">
        function open_menu() {
            let clicked = document.getElementById('drop-menu');
            if (clicked.style.display == 'block') {
                clicked.style.display = 'none';
            }
            else {
                clicked.style.display = 'block';
            }
        }
    </script>
            
<header tabindex="-1" data-testid="stHeader" class="st-emotion-cache-1avcm0n ezrtsby2">
        <div id="dropdown">
        <button onclick="open_menu()">Click Me!</button>
        <div class="open" id="drop-menu">
            <ul>
                <li><a href="https://swineline.streamlit.app/~/+/">Item-1</a></li>
                <li><a href="https://swineline.streamlit.app/~/+/marketplace">Item-2</a></li>
                <li><a href="">Item-3</a></li>
                <li><a href="">Item-4</a></li>
            </ul>
        </div>
        </div>
        <ul>
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


