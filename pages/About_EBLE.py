import streamlit as st

st.set_page_config(
    page_title="About EBLE",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 About EBLE")

st.markdown("""
# Empowering Every Business to Level Up

EBLE is an AI-powered business intelligence and financial empowerment platform
designed specifically for micro-businesses, kirana stores, street vendors,
tea stalls, dairy businesses, and small retailers.

Our goal is to help small businesses digitize operations, gain financial visibility,
access credit opportunities, and make smarter business decisions using AI.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("❌ Problem Statement")

    st.error("""
    • Most small businesses maintain manual records

    • Limited financial visibility

    • Difficulty accessing loans and funding

    • No business intelligence tools

    • Lack of digital adoption

    • Poor forecasting and planning
    """)

with col2:

    st.subheader("✅ Our Solution")

    st.success("""
    • Revenue Tracking

    • Expense Management

    • AI Business Advisor

    • AI Revenue Forecasting

    • Financial Readiness Assessment

    • Credit Hub

    • OCR Receipt Digitization

    • Multi-Language Support
    """)

st.markdown("---")

st.subheader("🎯 Target Users")

st.info("""
🏪 Kirana Stores

☕ Tea Stalls

🥛 Dairy Businesses

🛒 Small Retail Shops

🚚 Street Vendors

🏬 Local Traders

📦 Micro Businesses
""")

st.markdown("---")

st.subheader("🌟 Key Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.success("""
    📊 Analytics Dashboard

    💰 Revenue Tracking

    💸 Expense Tracking

    📈 Profit Analysis
    """)

with feature2:
    st.success("""
    🤖 AI Advisor

    🔮 AI Forecasting

    📑 Financial Readiness

    🏦 Credit Hub
    """)

with feature3:
    st.success("""
    📷 OCR Scanner

    🌐 Language Support

    📰 Market Intelligence

    💎 Premium Features
    """)

st.markdown("---")

st.subheader("📈 Business Impact")

impact1, impact2, impact3, impact4 = st.columns(4)

with impact1:
    st.metric("Businesses", "5+")

with impact2:
    st.metric("Modules", "12+")

with impact3:
    st.metric("AI Features", "4+")

with impact4:
    st.metric("Languages", "3")

st.markdown("---")

st.subheader("🚀 Vision")

st.warning("""
EBLE aims to become India's Operating System for Micro-Businesses.

By combining AI, Financial Inclusion, Digital Record Keeping,
Business Intelligence, and Credit Discovery into a single platform,
EBLE empowers every small business to grow, compete, and thrive.
""")

st.markdown("---")

st.subheader("🏆 Why EBLE?")

st.success("""
Record → Analyze → Forecast → Fund → Grow

EBLE transforms small businesses from paper-based operations
into AI-powered growth-driven enterprises.
""")

from utils.theme import apply_theme

apply_theme()