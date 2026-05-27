import streamlit as st
import pandas as pd
from pathlib import Path

# Displaying image on sidebar
# Displaying image on sidebar
with st.sidebar:
    st.image("car_steamlit.jpg", width=254)
 

# Page Configuration
st.set_page_config(
    page_title="Electric Car Market  Analytics",
    page_icon="🚗",
    layout="centered"
)

# 1. Your main title
st.title("⚡EV Market Analytics⚡")

# 2. Create columns: left one takes up space, right one holds the text
col1, col2 = st.columns([4, 1])

with col2:
    st.write("— Supriya Gir   ")

# ------------------------------
# CUSTOM CSS (FIXED SIDEBAR BUTTONS)
# ------------------------------
st.markdown("""
<style>
/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color:#053827 !important;
}

/* Sidebar button wrapper */
section[data-testid="stSidebar"] div.stButton {
    width: 250px;
}

/* Sidebar buttons full width */
section[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    display: flex !important;
    justify-content: flex-start !important;
    border-radius: 10px;
    margin-bottom: 8px;
    padding-left: 12px;
}

/* Hover effect */
section[data-testid="stSidebar"] div.stButton > button:hover {
    background-color:  #fff9dc;
}

/* Main app background */
.stApp {
    background-color: #fff9dc;
}

/* Headings */
h1, h2, h3, p {
    color: #002366;
}

/* Section title */
.section-title {
    font-size: 40px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 15px;
    color: #002366;
}
            

/* Target the sidebar container background and text */
    [data-testid="stSidebar"] {
        color: white;
    }
    
/* Target text within the sidebar (headers, labels, etc.) */
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: white !important;
    }
            
/* Target links inside the sidebar */
    [data-testid="stSidebar"] a {
        color: white !important;
</style>
""", unsafe_allow_html=True)


st.sidebar.write("---")

# ------------------------------
# PAGE ROUTING
# ------------------------------

st.markdown("<div class='section-title'><span style='font-size:26px'>📊 </span>Introduction</div>", unsafe_allow_html=True)
st.markdown("""
    <div style="font-size: 18px; line-height: 1.6;">
    The electric vehicle (EV) industry is evolving rapidly, driven by advancements in 
    battery technology, shifting consumer preferences, and increasing competition among 
    global manufacturers. But what truly defines success in this market? Is it 
    performance, price, range or something deeper like brand power?
    </div>
    """, unsafe_allow_html=True)


st.markdown("<div class='section-title'><span style='font-size:32px'>🎯</span>Objective</div>", unsafe_allow_html=True)
st.markdown("""
    <div style="font-size: 18px; line-height: 1.6;">
The goal of this project is to demonstrate how data from the EV industry can be transformed into an interactive analytical tool that helps users understand:

⚡ Market growth patterns<br>
⚡ Pricing variations across segments<br>
⚡ Key performance factors influencing EV adoption
    
    
    """, unsafe_allow_html=True)

st.markdown("<div class='section-title'><span style='font-size:32px'>🛠️</span>Tools & Technologies</div>", unsafe_allow_html=True)
st.markdown("""
    <div style="font-size: 18px; line-height: 1.6;">
⚡Python (Pandas, NumPy)<br>
⚡Streamlit<br>
⚡Power BI<br>
⚡Kaggle Dataset: Electric Vehicle Market and Pricing Dataset (2026)
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.markdown("""
🔗 Power BI Dashboard:  
👉 [Click here to view dashboard](https://app.powerbi.com/groups/me/reports/23963ba2-b909-4f82-829b-1ad909e70ffc/30e231deff780b246496?experience=power-bi&clientSideAuth=0)
""")

st.write("---")

st.warning(
        "⚠️ Disclaimer: This app is for educational purposes only. "
)
