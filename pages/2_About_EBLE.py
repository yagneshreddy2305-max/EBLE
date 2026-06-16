import streamlit as st

from utils.theme import apply_theme

st.set_page_config(
    page_title="About EBLE",
    page_icon="🚀",
    layout="wide"
)

apply_theme()

# HERO SECTION
st.markdown("""
<div class="hero">

<h1>🚀 EBLE</h1>

<h3>Empowering Every Business to Level Up</h3>

<p>
AI-Powered Business Intelligence Platform for Small Businesses,
Vendors, Retailers and Rural Entrepreneurs.
</p>

</div>
""", unsafe_allow_html=True)

# ABOUT
st.markdown("""
### 🌍 About EBLE

EBLE is an AI-powered business intelligence and financial empowerment platform
designed for small businesses that often operate without digital tools.

Our mission is to help business owners record transactions, understand performance,
forecast growth, improve financial readiness, and access funding opportunities.
""")

st.markdown("---")

# PROBLEM & SOLUTION
col1, col2 = st.columns(2)

with col1:

    st.subheader("❌ Challenges Faced by Small Businesses")

    st.error("""
• Manual record keeping

• Poor financial visibility

• Difficulty accessing credit

• Lack of business insights

• Limited digital adoption

• No forecasting tools

• Weak financial documentation
""")

with col2:

    st.subheader("✅ How EBLE Solves It")

    st.success("""
• Revenue Tracking

• Expense Management

• AI Business Advisor

• AI Forecasting

• Financial Readiness Scoring

• Credit Discovery

• OCR Receipt Digitization

• Multi-Language Support
""")

st.markdown("---")

# TARGET USERS
st.subheader("🎯 Who EBLE Serves")

st.info("""
🏪 Retail & Kirana Stores

🚚 Street Vendors & Mobile Sellers

🧵 Local Manufacturing Businesses

🌾 Rural & Agri-Linked Enterprises

📦 Wholesale & Distribution Businesses

💄 Beauty & Service Businesses

👩‍💼 First-Time Entrepreneurs
""")

st.markdown("---")

# FEATURES
st.subheader("🌟 Core Capabilities")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.success("""
📊 Business Analytics

💰 Revenue Monitoring

💸 Expense Intelligence

📈 Profit Optimization
""")

with feature2:
    st.success("""
🤖 AI Business Advisor

🔮 Growth Forecasting

📑 Financial Readiness

🏦 Credit Discovery
""")

with feature3:
    st.success("""
📷 OCR Digitization

🌐 Multi-Language Access

📰 Market Intelligence

🚀 Growth Recommendations
""")

st.markdown("---")

# BUSINESS IMPACT
st.subheader("📈 Business Impact")

impact1, impact2, impact3, impact4 = st.columns(4)

with impact1:
    st.metric("Target MSMEs", "65M+")

with impact2:
    st.metric("Platform Modules", "12+")

with impact3:
    st.metric("AI Engines", "4")

with impact4:
    st.metric("Languages", "3+")

st.markdown("---")

# VISION
st.subheader("🚀 Vision")

st.warning("""
EBLE aims to become India's Operating System for Small Businesses.

By combining AI, Business Intelligence, Financial Readiness,
Credit Discovery and Digital Record Keeping into one platform,
EBLE empowers businesses to grow confidently and sustainably.
""")

st.markdown("---")

# FUTURE ROADMAP
st.subheader("🛣️ Future Roadmap")

phase1, phase2, phase3 = st.columns(3)

with phase1:

    st.success("""
### Phase 1

✅ Revenue Tracking

✅ Expense Management

✅ Analytics Dashboard

✅ AI Advisor

✅ AI Forecasting

✅ Financial Readiness
""")

with phase2:

    st.info("""
### Phase 2

🔄 UPI Integration

🔄 GST Analytics

🔄 WhatsApp Integration

🔄 Smart Invoicing

🔄 Automated Bookkeeping

🔄 Business Alerts
""")

with phase3:

    st.warning("""
### Phase 3

🚀 Embedded Lending

🚀 Credit Marketplace

🚀 Vendor Intelligence

🚀 Voice AI Assistant

🚀 Supply Chain Insights

🚀 Nationwide Expansion
""")

st.markdown("---")

# FINAL MESSAGE
st.subheader("🏆 Why EBLE?")

st.success("""
Record → Analyze → Forecast → Fund → Grow

EBLE transforms small businesses from paper-based operations
into AI-powered, data-driven enterprises.
""")
