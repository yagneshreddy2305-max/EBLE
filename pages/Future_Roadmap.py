import streamlit as st

st.set_page_config(
    page_title="Future Roadmap",
    page_icon="🚀",
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
st.title("🚀 Future Roadmap")

st.success("""
Phase 2

• E-Billing
• GST Tracking
• Inventory Management
• AI Sales Prediction
• UPI Integration
""")

st.info("""
Phase 3

• Voice Assistant
• Bank Integrations
• Loan Marketplace
• Vendor Credit Score
""")

from utils.theme import apply_theme

apply_theme()