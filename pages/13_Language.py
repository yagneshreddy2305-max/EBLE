import streamlit as st

st.set_page_config(
    page_title="Language Settings",
    page_icon="🌐",
    layout="wide"
)
st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(90deg,#00E5FF,#0066FF);
color:white;
">

<h1>🚀 EBLE</h1>

<h3>Empowering Every Business to Level Up</h3>

<p>
AI-Powered Business Intelligence Platform
for Small Businesses, Vendors and Retailers.
</p>

</div>
""", unsafe_allow_html=True)

st.title("🌐 Language Support")

language = st.selectbox(
    "Select Language",
    [
        "English",
        "Hindi",
        "Telugu"
    ]
)

st.markdown("---")

if language == "English":

    st.success("Language Changed to English")

    st.markdown("""
### Welcome to EBLE

Empowering Every Business to Level Up

Track Revenue

Track Expenses

AI Business Insights

Financial Readiness

Credit Opportunities
""")

elif language == "Hindi":

    st.success("भाषा हिंदी में बदल दी गई")

    st.markdown("""
### EBLE में आपका स्वागत है

हर व्यवसाय को आगे बढ़ाने का लक्ष्य

राजस्व ट्रैक करें

खर्च ट्रैक करें

AI व्यापार सलाह

वित्तीय तैयारी

ऋण और योजनाएं
""")

elif language == "Telugu":

    st.success("భాష తెలుగు లోకి మార్చబడింది")

    st.markdown("""
### EBLE కి స్వాగతం

ప్రతి వ్యాపారాన్ని అభివృద్ధి చేయడం మా లక్ష్యం

ఆదాయాన్ని ట్రాక్ చేయండి

ఖర్చులను ట్రాక్ చేయండి

AI వ్యాపార సలహాలు

ఆర్థిక సిద్ధత

రుణ అవకాశాలు
""")

from utils.theme import apply_theme

apply_theme()