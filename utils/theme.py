import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    .block-container{
        padding-top:1rem;
        padding-bottom:1rem;
        max-width:1400px;
    }

    [data-testid="stMetric"]{
        background:#1C1F26;
        border:1px solid #2D3748;
        border-radius:18px;
        padding:20px;
        box-shadow:0px 6px 20px rgba(0,0,0,0.25);
    }

    .hero{
        padding:30px;
        border-radius:20px;
        background:linear-gradient(90deg,#00E5FF,#0066FF);
        color:white;
        margin-bottom:20px;
    }

    .glass{
        background:#1C1F26;
        border:1px solid #2D3748;
        padding:20px;
        border-radius:18px;
    }

    </style>
    """, unsafe_allow_html=True)