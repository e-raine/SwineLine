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
                <img src="https://previews.dropbox.com/p/thumb/ACMh5nmVaEEDN50H094PSVbIQntAMqANgZLQGjz7AVp1Hm05p_Q0q5bkz-ohq2Qb6Ucwh2Wz6Ualqlfm5GKP0SWXbeYUcmaunSsqL4F6GHIe7ZyHlY8ioWNMtwiO65CEW4rWnL7bkqg6zeDg1Zp5gPvY_w1jB8YNwKxuELfp3xiCOu3wUAu8jkcAfUpDzKD5WKQGfBlh01ovPsERiyp3mLr0_GY1yi6_KziLmzOfCmzoWL97NQqsSvXlx8tRQkiiyB3-rC7eWDG4-vaEEL8fot7y9xTeid25drsURt5kyCE6kPoPw9_0GMlzVlvSxWicfIM_J_lrbO05gr2wW9mNX55s/p.png" style="width: 64px; height: 64px;">
                <img src="https://previews.dropbox.com/p/thumb/ACMLkEOREWGH0GHzUI1kzQl-B2IVtisLvwd_T_Bn2HEtCYqAHB2UF3wbkk4Ovi8tWP8NxsaTAanPKol4rPL_9qI4_dX6KD6UvINzloHANvJ60kDEtJLPkxoBlZDqP4mM31ao-CXDIrb2D90NxQnGGiDnG6L45gsHObLVtHw2s1MrO8g2uInj4mA2uTP1gxobDbWh8OFxxmiH9zCAOgO3gZNte4A5FCUW2ArpY63KzX5stYLhKXnv9u3SxKojEwuFY9CTNVdUKov4tzNxTG4g-MDw_8noNRyES41DdOmVMXHMSp0dz4Mx5mrs-beoVmRUGfvrt9vRVNE8-M3Qo0tBvQK6/p.png" style="width: 113.78px; height: 64px;">
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
